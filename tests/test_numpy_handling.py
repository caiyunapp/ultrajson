# coding=UTF-8
from __future__ import print_function, unicode_literals

import numpy as np
import six

import nujson

if six.PY2:
    import unittest2 as unittest
else:
    import unittest


class nujsonValidatingNumpy(unittest.TestCase):

    def test_np_int64(self):
        d = {
            "a": np.int64(1)
        }
        self.assertEqual(nujson.dumps(d), '{"a":1}')

    def test_np_float32(self):
        d = {
            "a": np.float32(1.2)
        }
        self.assertEqual(nujson.dumps(d), '{"a":1.2}')


if __name__ == "__main__":
    unittest.main()
