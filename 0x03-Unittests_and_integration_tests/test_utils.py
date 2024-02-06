#!/usr/bin/env python3
''' Parameterize a unit test '''
import utils
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from fixtures import TEST_PAYLOAD


class TestAccessNestedMap(unittest.TestCase):
    ''' test access nested map '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
        # self.assertIn(repr(expected_key), str(context.exception))


# class TestGetJson(unittest.TestCase):
#     ''' Mock HTTP calls '''

#     @patch()
#     def test_get_json(self):
#         pass
