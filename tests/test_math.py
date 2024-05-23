# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Author: Kyle Lahnakoski (kyle@lahnakoski.com)
#
import math
import random
from math import floor

from mo_testing.fuzzytestcase import FuzzyTestCase

import mo_math
from mo_math import randoms, almost_equal


class TestMath(FuzzyTestCase):
    def test_isnumber(self):
        assert mo_math.is_number(9999999999000)

    def test_mod(self):
        self.assertEqual(mo_math.mod(12, 12), 0)
        self.assertEqual(mo_math.mod(11, 12), 11)
        self.assertEqual(mo_math.mod(2, 12), 2)
        self.assertEqual(mo_math.mod(1, 12), 1)
        self.assertEqual(mo_math.mod(-0, 12), 0)
        self.assertEqual(mo_math.mod(-1, 12), 11)
        self.assertEqual(mo_math.mod(-2, 12), 10)
        self.assertEqual(mo_math.mod(-12, 12), 0)

    def test_floor(self):
        self.assertEqual(mo_math.floor(0, 1), 0)
        self.assertEqual(mo_math.floor(1, 1), 1)
        self.assertEqual(mo_math.floor(-1, 1), -1)
        self.assertEqual(mo_math.floor(0.1, 1), 0)
        self.assertEqual(mo_math.floor(1.1, 1), 1)
        self.assertEqual(mo_math.floor(-1.1, 1), -2)

        self.assertEqual(mo_math.floor(0, 2), 0)
        self.assertEqual(mo_math.floor(1, 2), 0)
        self.assertEqual(mo_math.floor(-1, 2), -2)
        self.assertEqual(mo_math.floor(0.1, 2), 0)
        self.assertEqual(mo_math.floor(1.1, 2), 0)
        self.assertEqual(mo_math.floor(-1.1, 2), -2)
        self.assertEqual(mo_math.floor(-10, 2), -10)

    def test_floor_mod_identity(self):
        for i in range(100):
            x = randoms.float()*200 - 100.0
            m = abs(random.gauss(0, 5))

            self.assertAlmostEqual(mo_math.floor(x, m)+mo_math.mod(x, m), x, places=7)

    def test_floor_mod_identity_w_ints(self):
        for i in range(100):
            x = randoms.float()*200 - 100.0
            m = floor(abs(random.gauss(0, 5)))

            if m == 0:
                self.assertEqual(mo_math.floor(x, m), None)
                self.assertEqual(mo_math.mod(x, m), None)
            else:
                self.assertAlmostEqual(mo_math.floor(x, m)+mo_math.mod(x, m), x, places=7)

    def test_round(self):
        self.assertAlmostEqual(mo_math.round(3.1415, digits=0), 1)
        self.assertAlmostEqual(mo_math.round(3.1415, digits=4), 3.142)
        self.assertAlmostEqual(mo_math.round(4, digits=0), 10)
        self.assertAlmostEqual(mo_math.round(11, digits=0), 10)
        self.assertAlmostEqual(mo_math.round(3.1415), 3)

    def test_random_hex(self):
        self.assertEqual(len(randoms.hex(5)), 5)

    def test_to_float(self):
        self.assertEqual(mo_math.to_float(1), 1.0)
        self.assertEqual(mo_math.to_float("1"), 1.0)
        self.assertEqual(mo_math.to_float("1.0"), 1.0)
        self.assertEqual(mo_math.to_float("1.1"), 1.1)
        self.assertEqual(mo_math.to_float("1.1a"), None)

    def test_raises_when_different1(self):
        self.assertFalse(almost_equal(1, 0.1, 6))

    def test_raises_when_different2(self):
        self.assertFalse(almost_equal(1.000001, 1.000002, 7))

    def test_raises_when_different3(self):
        self.assertFalse(almost_equal(1.000001, 1.0000016, 7))

    def test_raises_when_different4(self):
        self.assertFalse(almost_equal(1.000001, 1.0000015, digits=7))

    def test_ok_when_same1(self):
        self.assertTrue(almost_equal(1.000001, 1.0000011, digits=7))

    def test_ok_when_same2(self):
        self.assertTrue(almost_equal(1.000002, 1.0000025, digits=7))

    # tests for number of significant digits (places)
    def test_raises_when_different_places1(self):
        self.assertFalse(almost_equal(1.0001, 1.0002, places=5))

    def test_raises_when_different_places2(self):
        self.assertFalse(almost_equal(1.0001, 1.00016, places=5))

    def test_raises_when_different_places3(self):
        self.assertFalse(almost_equal(100.01, 100.016, places=5))

    def test_raises_when_different_places4(self):
        self.assertFalse(almost_equal(0.0010001, 0.00100016, places=5))

    def test_raises_when_different_places5(self):
        self.assertTrue(almost_equal(100, 100.4, places=3))

    def test_ok_when_same_places1(self):
        self.assertTrue(almost_equal(1.0001, 1.0001499999, places=5))

    def test_ok_when_same_places5(self):
        self.assertTrue(almost_equal(1.0002, 1.0002499999, places=5))

    def test_ok_when_same_places2(self):
        self.assertTrue(almost_equal(100.01, 100.015, places=5))

    def test_ok_when_same_places3(self):
        self.assertTrue(almost_equal(0.0010001, 0.00100015, places=5))

    def test_ok_when_same_places4(self):
        self.assertTrue(almost_equal(0.0010001, 0.00100016, places=4))


    def test_ceiling(self):
        self.assertEqual(mo_math.ceiling(0), 1)
        self.assertEqual(mo_math.ceiling(0.1), 1)
        self.assertEqual(mo_math.ceiling(1), 2)
        self.assertEqual(mo_math.ceiling(1.1), 2)
        self.assertEqual(mo_math.ceiling(-1), 0)
        self.assertEqual(mo_math.ceiling(-1.1), -1)

    def test_ceiling_7(self):
        self.assertEqual(mo_math.ceiling(0,7), 7)
        self.assertEqual(mo_math.ceiling(0.1,7), 7)
        self.assertEqual(mo_math.ceiling(8, 7), 14)
        self.assertEqual(mo_math.ceiling(1,7), 7)
        self.assertEqual(mo_math.ceiling(1.1,7), 7)
        self.assertEqual(mo_math.ceiling(-1,7), 0)
        self.assertEqual(mo_math.ceiling(-1.1,7), 0)
        self.assertEqual(mo_math.ceiling(-8, 7), -7)

    def test_builtin_ceiling(self):
        self.assertEqual(math.ceil(0), 0)
        self.assertEqual(math.ceil(0.1), 1)
        self.assertEqual(math.ceil(1), 1)
        self.assertEqual(math.ceil(1.1), 2)
        self.assertEqual(math.ceil(-1), -1)
        self.assertEqual(math.ceil(-1.1), -1)

