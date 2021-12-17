import unittest
import sys
  
# import your solution below
from midB_sol import *


class Q1BTestCase (unittest.TestCase):
	""" tests for average functions """

	def test1_noarg (self):
		self.assertFalse(has_a_repeater())

	def test1_1arg (self):
		self.assertFalse(has_a_repeater(k1=2))

	def test1_argsnorepeater(self):
		self.assertFalse(has_a_repeater(k1=2,k2=4,k3=0,k4=-1))

	def test1_argsrepeaters(self):
		self.assertTrue(has_a_repeater(k1=2,k2=4,k3=2,k4=0,k5=-1,k6=4))

	def test1_example1(self):
		self.assertTrue(has_a_repeater(k1=1,k2=2,k3=4,k4=2,k5=4,k6=2))

	def test1_example2(self):
		self.assertFalse(has_a_repeater(k1="ding",k2= "dong",k3= 3))


class Q2BTestCase (unittest.TestCase):
	""" tests for average functions """

	def test1_argemptylist (self):
		self.assertCountEqual(find_singles([]), [])

	def test1_1arg (self):
		self.assertCountEqual(find_singles([3]), [3])

	def test1_argsnorepeater (self):
		self.assertCountEqual(find_singles([3, 4, 90, -1, "sing"]), [3, 4, 90, -1, "sing"])

	def test1_argsrepeaters(self):
		self.assertCountEqual(find_singles([3,4,3,-1,"sing",90, -1, "sing"]), [4,90])


class Q3BTestCase (unittest.TestCase):

	@unittest.skip("was not part of acceptable solution!")
	def test1_argemptylist (self):
		self.assertEqual(max_profit([]), [])

	def test1_example1(self):
		self.assertEqual(max_profit([7, 3, 6, 12, 5, 1, 4, 8]), (1,3))

	def test1_example2(self):
		self.assertEqual(max_profit([7, 3, 6, 9, 5, 1, 4, 8]), (5,7))

	# this one may not adhere to "striclty increasing" clause
	# same applies to 1arg
	def test1_example3(self):
		self.assertEqual(max_profit([7, 6, 5, 4, 1]), (0,0))



if __name__ == '__main__':
	print("in main")
	unittest.main()
