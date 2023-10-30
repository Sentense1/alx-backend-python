#!/usr/bin/env python3
"""
Module for unittest using parameterized
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Class for unittest case
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Method to test nexted map function. """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):  # noqa
        """ Test method for nested_map tp raise exception """
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test class for testing the get json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Method to test get_json function"""
        config = {'return_value.json.return_value': test_payload}

        patcher = patch('requests.get', **config)

        mock = patcher.start()

        self.assertEqual(get_json(test_url), test_payload)

        mock.assert_called_once()

        patcher.stop()


class TestMemoize(unittest.TestCase):
    """
    Test class for memoise function
    """
    def test_memoize(self):
        """
        method for testing memoize function
        """
        class TestClass:
            """
            A test class for wrapping
            """

            def a_method(self):
                """
                Method of test class
                """
                return 42

            @memoize
            def a_property(self):
                """
                A decorator method
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
