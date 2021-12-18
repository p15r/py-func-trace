# py_func_trace
`py_func_trace` is a Python Pip package that provides functions to log
arguments and return values when a function is called, or exits, respectively.
Sensitive arguments are camouflaged if variable names are prefixed with
`priv_`.

## Packaging
- Install build tool: `python3 -m pip install --upgrade build`
- Create build: `cd py_func_trace && python3 -m build`
- Artefacts:
  ```bash
  ls dist/
  py_func_trace-0.1.0-py3-none-any.whl  # build distribution
  py_func_trace-0.1.0.tar.gz            # source archive
  ```

## Usage
- Install: `python3 -m pip install dist/py_func_trace-0.1.0-py3-none-any.whl`
- Use:
  ```python
  import inspect
  from py_func_trace import func_trace

  import logging
  import sys
  logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

  def test(a: str, priv_b: str) -> str:
      func_trace.enter(inspect.currentframe())
      ret = "return value"
      func_trace.leave(inspect.currentframe(), ret)
      return ret

  test("arg1", "arg2_sensitive")

  """
  Output:
  INFO:py_func_trace.func_trace:(t.py:8) Entering "test" args: {'a': 'arg1', 'priv_b': '******'}
  INFO:py_func_trace.func_trace:(t.py:8) Exiting "test" ret: return value
  """
  ```
- Run tests: `python3 setup.py test`
