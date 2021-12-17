import unittest
import sys
  
# import your solution below
from midA_sol import *

class Q1ATestCase (unittest.TestCase):
	""" tests for average functions """

	def test1_noarg (self):
		self.assertFalse(has_a_repeater())

	def test1_1arg (self):
		self.assertFalse(has_a_repeater(2))

	def test1_argsnorepeater(self):
		self.assertFalse(has_a_repeater(2,4,0,-1))

	def test1_argsrepeaters(self):
		self.assertTrue(has_a_repeater(2,4,2,0,-1,4))

	def test1_example1(self):
		self.assertTrue(has_a_repeater(1,2,4,2,4,2))

	def test1_example2(self):
		self.assertFalse(has_a_repeater("ding", "dong", 3))


class Q2ATestCase (unittest.TestCase):

	def test1_argemptylist (self):
		self.assertCountEqual(find_repeaters([]), [])

	def test1_1arg (self):
		self.assertCountEqual(find_repeaters([3]), [])

	def test1_argsnorepeater (self):
		self.assertCountEqual(find_repeaters([3, 4, 90, -1, "sing"]), [])

	def test1_argsrepeaters(self):
		self.assertCountEqual(find_repeaters([3,4,3,-1,"sing",90, -1, "sing"]), [3,-1,"sing"])


class Q3ATestCase (unittest.TestCase):

	@unittest.skip("was not part of acceptable solution!")
	def test1_argemptylist (self):
		self.assertEqual(long_subseq([]), [])

	def test1_example1(self):
		self.assertEqual(long_subseq([2,3,4,5,2]), [2,3,4,5])

	def test1_example2(self):
		self.assertEqual(long_subseq([2,3,4,-9,-5,-3,-1,2,3,1]), [-9,-5,-3,-1,2,3])

	# this one may not adhere to "striclty increasing" clause
	# same applies to 1arg
	def test1_example3(self):
		self.assertEqual(long_subseq([3,3,3,3]), [3])



if __name__ == '__main__':
	print("in main")
	unittest.main()
