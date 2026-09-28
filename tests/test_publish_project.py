import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
spec = importlib.util.spec_from_file_location(
    "publisher", Path(__file__).resolve().parents[1] / "scripts/publish_project.py"
)
publisher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publisher)


class PublishRetryTests(unittest.TestCase):
    def test_refreshes_catalogue_and_retries_a_concurrent_push(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "projects").mkdir()
            (root / "projects/acme--tool.md").write_text(
                '---\nrepository: "acme/tool"\nsummary: "A tool"\ntopics: ["demo"]\n---\n'
            )
            calls = []

            def fake_git(*args):
                calls.append(args)
                if args[:1] == ("push",) and sum(c[:1] == ("push",) for c in calls) == 1:
                    return subprocess.CompletedProcess(args, 1, "", "! [rejected] HEAD -> main (fetch first)")
                if args[:2] == ("diff", "--cached"):
                    return subprocess.CompletedProcess(args, 1, "", "")
                return subprocess.CompletedProcess(args, 0, "", "")

            with patch.object(publisher, "ROOT", root), \
                    patch.object(publisher, "git", side_effect=fake_git), \
                    patch.object(publisher.index_project, "build_index", wraps=publisher.index_project.build_index) as build_index:
                publisher.publish("projects/acme--tool.md", "main", 12, sleep=lambda _: None)

            self.assertEqual(sum(c[:1] == ("push",) for c in calls), 2)
            self.assertEqual(sum(c[:1] == ("fetch",) for c in calls), 2)
            self.assertEqual(sum(c[:1] == ("reset",) for c in calls), 2)
            self.assertEqual(build_index.call_count, 2)

    def test_does_not_retry_a_non_retryable_push_failure(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "projects").mkdir()
            (root / "projects/acme--tool.md").write_text(
                '---\nrepository: "acme/tool"\nsummary: "A tool"\ntopics: ["demo"]\n---\n'
            )
            calls = []

            def fake_git(*args):
                calls.append(args)
                if args[:1] == ("push",):
                    return subprocess.CompletedProcess(args, 1, "", "permission denied")
                if args[:2] == ("diff", "--cached"):
                    return subprocess.CompletedProcess(args, 1, "", "")
                return subprocess.CompletedProcess(args, 0, "", "")

            with patch.object(publisher, "ROOT", root), patch.object(publisher, "git", side_effect=fake_git):
                with self.assertRaisesRegex(RuntimeError, "permission denied"):
                    publisher.publish("projects/acme--tool.md", "main", 12, sleep=lambda _: None)

            self.assertEqual(sum(c[:1] == ("push",) for c in calls), 1)


if __name__ == "__main__":
    unittest.main()
