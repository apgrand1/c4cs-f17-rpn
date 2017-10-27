import unittest

import rpn

class TestBasics(unittest.TestCase);
	def: testAdd(self);
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)

