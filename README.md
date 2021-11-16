# py_func_trace
Python package `py_func_trace` provides functions to log when a function
starts executing and before it exits. The log information includes
function parameters and return values. Sensitive values are camouflaged if
variables are prefixed with `priv_`.

- Install: `python3 -m pip install dist/py_func_trace-0.1.0-py3-none-any.whl`
- Use:
  ```python
  import inspect
  from py_func_trace import func_trace

  # for demo purposes:
  import sys
  logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

  func_trace.trace_enter(inspect.currentframe())
  ```

## Packaging
- Install build tool: `python3 -m pip install --upgrade build`
- Create build: `python3 -m build`
- Artefacts:
  ```bash
  ls dist/
  py_func_trace-0.1.0-py3-none-any.whl  # build distribution
  py_func_trace-0.1.0.tar.gz            # source archive
  ```
