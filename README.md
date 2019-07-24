# The UltraJSON Fork That Support Numpy Serialization

![](https://travis-ci.org/caiyunapp/ultrajson.svg?branch=numpy)

- Original author: [xtao (Xu Tao)](https://github.com/xtao)
- Inspired by [Pandas' ujson](https://github.com/pandas-dev/pandas/tree/master/pandas/_libs/src/ujson/python)

## Environment

Test on Ubuntu 18.04 with Python3.7

Known issue: macOS support.

## How to install

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
