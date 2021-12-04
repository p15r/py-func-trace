"""Test module for py-func-trace"""

import logging
import inspect
import sys
import io
from typing import Dict
from unittest import TestCase, mock

from py_func_trace import func_trace

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class TestAll(TestCase):
    """Test class for py-func-trace"""
    @staticmethod
    def fixture_func(
        i: int, a_string: str, priv_foo: int, dic: Dict[str, str]
    ) -> Dict[str, str]:
        """Testing all functionality in one go."""
        func_trace.enter(inspect.currentframe())

        print(f"i: {i}, a_string: {a_string}, priv_foo: {priv_foo},dic: {dic}")

        ret = {"a": "s", "priv_b": "secret"}
        func_trace.leave(inspect.currentframe(), ret)
        return ret

    def test_is_string(self):
        """Tests return value"""
        ret = self.fixture_func(
            5, "b", 123, {"foo": "s", "priv_bar": "secret"}
        )
        self.assertTrue(isinstance(ret, dict))

    def test_print(self):
        """Test print output"""
        expected_stdout = ("i: 5, a_string: b, priv_foo: 123,"
                           "dic: {'foo': 's', 'priv_bar': 'secret'}")

        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.fixture_func(5, "b", 123, {"foo": "s", "priv_bar": "secret"})
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_stdout)

    def test_trace(self):
        """Test logging output"""
        expected_output = []
        expected_output.append("call('(%s:%s) Entering \"%s\" args: %s', "
                               "'test_all.py', 17, 'fixture_func', {'i': 5, "
                               "'a_string': 'b', 'priv_foo': '******', "
                               "'dic': {'foo': 's', 'priv_bar': '******'}})")

        expected_output.append("call('(%s:%s) Exiting \"%s\" ret: %s', "
                               "'test_all.py', 17, 'fixture_func', {'a': "
                               "'s', 'priv_b': 'secret'})")

        logger = logging.getLogger("py_func_trace.func_trace")
        with mock.patch.object(logger, 'info') as mock_info:
            self.fixture_func(5, "b", 123, {"foo": "s", "priv_bar": "secret"})
            mock_info.assert_called()
            self.assertEqual(
                expected_output[0],
                mock_info.mock_calls[0].__str__()
            )
            self.assertEqual(
                expected_output[1],
                mock_info.mock_calls[1].__str__()
            )

    def test___shorten_string(self):
        """Test string shortening"""
        shortened_string = 77 * 'b' + '...'
        expected_output = ("call('(%s:%s) Entering \"%s\" args: %s', "
                           "'test_all.py', 17, 'fixture_func', {'i': 5, "
                           f"'a_string': '{shortened_string}', 'priv_foo': "
                           "'******', "
                           "'dic': {'foo': 's', 'priv_bar': '******'}})")

        logger = logging.getLogger("py_func_trace.func_trace")
        with mock.patch.object(logger, 'info') as mock_info:
            self.fixture_func(
                5, 85 * "b", 123, {"foo": "s", "priv_bar": "secret"}
            )
            mock_info.assert_called()
            self.assertEqual(
                expected_output,
                mock_info.mock_calls[0].__str__()
            )
