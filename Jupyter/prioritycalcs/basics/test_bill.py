from unittest import TestCase
import unittest
import numpy as np
import numpy.testing as npt

import basics.eigen as eigen
import basics.bill as bill

testmat1 = np.array([[1, 2, 6.], [0.5, 1, 3], [1 / 6., 1 / 3., 1]])


class TestBill(TestCase):

    def test_eigen(self):
        expected = np.array([0.6, 0.3, 0.1])
        calc = eigen.largest_eigen(testmat1)
        npt.assert_almost_equal(calc, expected)

    def test_bepriority(self):
        expected = np.array([0.6, 0.3, 0.1])
        calc = bill.be_priorities(testmat1)
        npt.assert_almost_equal(calc, expected)

if __name__ == '__main__':
    unittest.main()
