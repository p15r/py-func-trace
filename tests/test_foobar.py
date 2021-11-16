import logging
import inspect
import sys
from typing import Dict
from unittest import TestCase

from py_func_trace import func_trace

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class TestAll(TestCase):
    def foobar(
            self, i: int, s: str, priv_foo: int, bar: Dict[str, str]
            ) -> Dict[str, str]:
        func_trace.trace_enter(inspect.currentframe())

        print(f"i: {i}, s:{s}, priv_foo: {priv_foo}, bar: {bar}")

        ret = {"a": "s", "priv_b": "secret"}
        func_trace.trace_exit(inspect.currentframe(), ret)
        return ret

    def test_is_string(self):
        # TODO: add moar tests (also parse stdoutput and check for camouflage
        ret = self.foobar(5, "b", 123, {"foo": "s", "priv_bar": "secret"})
        self.assertTrue(isinstance(ret, dict))
