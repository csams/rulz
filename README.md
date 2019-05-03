# rulz
A decorator based IoC framework for python3.6+. There are no runtime
dependencies outside of what's in the standard library.

A demo module is in `rulz/plugins/demo.py`.
```python
#!/usr/bin/env python
from rulz import plugin, run_graph


@plugin()
def one():
    return 1


@plugin()
def two():
    return 2


@plugin(one, two)
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(run_graph())
```

Invoke it directly or create a driver script like this:
```python
#!/usr/bin/env python
from rulz import load_components, run_graph


load_components("rulz.plugins")
print(run_graph())
```
