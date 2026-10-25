import json
import unittest
from pathlib import Path
from urllib.parse import urlparse


class PublicManifestTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(
            (Path(__file__).resolve().parents[1] / "license.json").read_text()
        )

    def test_device_list_is_absent_not_empty(self):
        self.assertNotIn("devices", self.manifest)

    def test_version_policy_survives_device_removal(self):
        minimum = self.manifest["minVersion"]
        latest = self.manifest["latestVersion"]
        self.assertIs(type(minimum), int)
        self.assertIs(type(latest), int)
        self.assertGreater(minimum, 0)
        self.assertGreaterEqual(latest, minimum)
        url = urlparse(self.manifest["apkUrl"])
        self.assertEqual("https", url.scheme)
        self.assertTrue(url.netloc)


if __name__ == "__main__":
    unittest.main()
