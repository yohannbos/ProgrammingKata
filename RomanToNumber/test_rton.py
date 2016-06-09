import unittest
from rton import converti

class TestRton(unittest.TestCase):
	def test_input_I_ouput_1(self):
		self.assertEqual(1, converti("I"))

	def test_input_III_ouput_3(self):
		self.assertEqual(3, converti("III"))

	def test_input_VI_ouput_6(self):
		self.assertEqual(6, converti("VI"))

	def test_input_IV_ouput_4(self):
		self.assertEqual(4, converti("IV"))

	def test_input_MCMLXXXVIII_ouput_1988(self):
		self.assertEqual(1988, converti("MCMLXXXVIII"))

	def test_input_MCMLXXVII_ouput_1977(self):
		self.assertEqual(1977, converti("MCMLXXVII"))

if __name__ == "__main__":
	unittest.main()
