"""Test module for py-func-trace"""

import logging
import inspect
import sys
import io
from typing import Dict
from unittest import TestCase

from py_func_trace import func_trace

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class TestAll(TestCase):
    """Test class for py-func-trace"""
    @staticmethod
    def all_in_one(
        i: int, a_string: str, priv_foo: int, dic: Dict[str, str]
    ) -> Dict[str, str]:
        """Testing all functionality in one go."""
        func_trace.enter(inspect.currentframe())

        print(f"i: {i}, a_string: {a_string}, priv_foo: {priv_foo},dic: {dic}")

        ret = {"a": "s", "priv_b": "secret"}
        func_trace.leave(inspect.currentframe(), ret)
        return ret

    def test_is_string(self):
        """Tests all_in_one()."""
        # TODO: test that captures logging (trace) info, not only prints
        #       redirect logging to stdout for this?
        ret = self.all_in_one(5, "b", 123, {"foo": "s", "priv_bar": "secret"})
        self.assertTrue(isinstance(ret, dict))

    def test_stdout(self):
        """to be done"""
        expected_stdout = ("i: 5, a_string: b, priv_foo: 123,"
                           "dic: {'foo': 's', 'priv_bar': 'secret'}")

        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.all_in_one(5, "b", 123, {"foo": "s", "priv_bar": "secret"})
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_stdout)
