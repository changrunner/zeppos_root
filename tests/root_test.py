import unittest
from zeppos_root.root import Root


class TestRootMethods(unittest.TestCase):
    def test_find_root_of_project(self):
        print(Root.find_root_of_project(__file__))
        # self.assertEqual(Root.find_root_of_project(__file__).
        #                  endswith("pyapp_300solutions_website_www-haegdorens-com\src\website"),
        #                  True)

if __name__ == '__main__':
    unittest.main()
