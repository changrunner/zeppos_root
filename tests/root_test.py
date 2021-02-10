import unittest
from zeppos_root.root import Root
from zeppos_logging.app_logger import AppLogger


class TestRootMethods(unittest.TestCase):
    def test_find_root_of_project(self):
        AppLogger.configure_and_get_logger("test")
        AppLogger.set_debug_level()
        self.assertTrue(Root.find_root_of_project(__file__).
                         endswith("zeppos_root"))


if __name__ == '__main__':
    unittest.main()
