# The UltraJSON Fork That Support Numpy Serialization

[![Build Status](https://travis-ci.org/caiyunapp/ultrajson.svg?branch=numpy)](https://travis-ci.org/caiyunapp/ultrajson)

- Original author: [xtao (Xu Tao)](https://github.com/xtao)
- Inspired by [Pandas' ujson](https://github.com/pandas-dev/pandas/tree/master/pandas/_libs/src/ujson/python)

## How to install

**Python 3.7 is required.**

```sh
git clone -b numpy https://github.com/caiyunapp/ultrajson
pip install -e .
# Don't use `python setup.py install`
```

## Example

```python
>>> import numpy as np
>>> import ujson
>>> a = {"a": np.int64(100)}
>>> ujson.dumps(a)
'{"a":100}'
>>> a["b"] = np.float64(10.9)
>>> ujson.dumps(a)
'{"a":100,"b":10.9}'
>>> a["c"] = np.str_("12")
>>> ujson.dumps(a)
'{"a":100,"b":10.9,"c":"12"}'
>>> a["d"] = np.array(list(range(10)))
>>> ujson.dumps(a)
'{"a":100,"b":10.9,"c":"12","d":[0,1,2,3,4,5,6,7,8,9]}'
>>> a["e"] = np.repeat(3.9, 4)
>>> ujson.dumps(a)
'{"a":100,"b":10.9,"c":"12","d":[0,1,2,3,4,5,6,7,8,9],"e":[3.9,3.9,3.9,3.9]}'
```

## Why make such a package and what is modified

On Python3, some data types of NumPy is not serializable. Here is some references we searched:

- [python - Why are some numpy datatypes JSON serializable and others not? - Stack Overflow](https://stackoverflow.com/questions/44459168/why-are-some-numpy-datatypes-json-serializable-and-others-not)
- [Maximum recursion level reached in Python 3 · Issue #221 · esnme/ultrajson](https://github.com/esnme/ultrajson/issues/221)
- [Issue 24313: json fails to serialise numpy.int64 - Python tracker](https://bugs.python.org/issue24313)

One solution is type conversion like: `int(numpy.int64)` and `numpy.array.tolist()`.
But it's not good for performance.
So we learned from [Pandas' ujson](https://github.com/pandas-dev/pandas/tree/master/pandas/_libs/src/ujson/python) and modified [the v1.35 ujson](https://github.com/esnme/ultrajson/releases/tag/v1.35).

The main point is convert NumPy data type in C, with calling NumPy's header. [Commit 187bd15](https://github.com/caiyunapp/ultrajson/commit/187bd155b7acd303aa6f5571f5b858c0d244edd6) has the most changes we made to support NumPy, and [Commit afedc42](https://github.com/caiyunapp/ultrajson/commit/afedc42b2ce288064821981acd70592342da55fa) fix a build issue on macOS caused by Clang.