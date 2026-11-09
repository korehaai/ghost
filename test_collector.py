import unittest

from ghost.collector import GhostCollector


class TestGhostCollector(unittest.TestCase):
    def test_collect_returns_expected_sections(self):
        collector = GhostCollector()
        result = collector.collect()
        self.assertIn("started_at", result)
        self.assertIn("finished_at", result)
        self.assertIn("system", result)
        self.assertIn("resources", result)
        self.assertIn("environment", result)
        self.assertIn("filesystem", result)

    def test_system_information_is_present(self):
        collector = GhostCollector()
        result = collector.collect()
        self.assertTrue(result["system"]["operating_system"])
        self.assertTrue(result["system"]["python_version"])

    def test_resource_values_are_non_negative(self):
        collector = GhostCollector()
        result = collector.collect()
        self.assertGreaterEqual(result["resources"]["home_disk_total_bytes"], 0)
        self.assertGreaterEqual(result["resources"]["home_disk_used_bytes"], 0)
        self.assertGreaterEqual(result["resources"]["home_disk_free_bytes"], 0)

    def test_collection_can_be_repeated(self):
        collector = GhostCollector()
        first = collector.collect()
        second = collector.collect()
        self.assertIn("finished_at", first)
        self.assertIn("finished_at", second)


if __name__ == "__main__":
    unittest.main()
