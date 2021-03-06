import unittest

from httprunner.loader import check


class TestLoaderCheck(unittest.TestCase):

    def test_is_function(self):
        func = lambda x: x + 1
        self.assertTrue(check.is_function(func))
        self.assertTrue(check.is_function(check.is_testcase))

    def test_is_testcases(self):
        data_structure = "path/to/file"
        self.assertFalse(check.is_testcases(data_structure))
        data_structure = ["path/to/file1", "path/to/file2"]
        self.assertFalse(check.is_testcases(data_structure))

        data_structure = {
            "project_mapping": {
                "PWD": "XXXXX",
                "functions": {},
                "env": {}
            },
            "testcases": [
                {  # testcase data structure
                    "config": {
                        "name": "desc1",
                        "path": "testcase1_path",
                        "variables": [],  # optional
                    },
                    "teststeps": [
                        # test data structure
                        {
                            'name': 'test step desc1',
                            'variables': [],  # optional
                            'extract': [],  # optional
                            'validate': [],
                            'request': {}
                        },
                        # test_dict2   # another test dict
                    ]
                },
                # testcase_dict_2     # another testcase dict
            ]
        }
        self.assertTrue(check.is_testcases(data_structure))
        data_structure = [
            {
                "name": "desc1",
                "config": {},
                "api": {},
                "testcases": ["testcase11", "testcase12"]
            },
            {
                "name": "desc2",
                "config": {},
                "api": {},
                "testcases": ["testcase21", "testcase22"]
            }
        ]
        self.assertTrue(data_structure)

    def test_is_variable(self):
        var1 = 123
        var2 = "abc"
        self.assertTrue(check.is_variable(("var1", var1)))
        self.assertTrue(check.is_variable(("var2", var2)))

        __var = 123
        self.assertFalse(check.is_variable(("__var", __var)))

        func = lambda x: x + 1
        self.assertFalse(check.is_variable(("func", func)))

        self.assertFalse(check.is_variable(("unittest", unittest)))
