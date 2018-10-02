#Monte Roybal
#Dr. Richard Medina
#Software Engineering
#Student Analytics Class Unittests

import unittest

from roybal_student_analytics import *

class Test_Roybal_Student_Analytics(unittest.TestCase):
	"""A collection of unit tests for the Roybal_Student_Analytics class. """
	def test_init(self):
		"""Unit test for Roybal_Student_Analytics constructor."""
		s = Student_Analytics()
		self.assertEqual(len(s.data),89)

	def test_classify_grade(self):
		"""Unit test for Roybal_Student_Analytics classify_grade method."""
		s = Student_Analytics()
		self.assertEqual(s.classify_grade(4.75),"A+")

	def test_element_count(self):
		"""Unit test for Roybal_Student_Analytics element_count method."""
		s = Student_Analytics()
		self.assertEqual(s.element_count(2,"F"),6)

	def test_avg_grade(self):
		"""Unit test for Roybal_Student_Analytics avg_grade method."""
		s = Student_Analytics()
		self.assertEqual(s.classify_grade(s.avg_grade(3)),"A-")

	def test_grade_change(self):
		"""Unit test for Roybal_Student_Analytics grade_change method."""
		s = Student_Analytics()
		self.assertEqual(int(s.grade_change()),0)

if __name__ == '__main__':
	unittest.main()