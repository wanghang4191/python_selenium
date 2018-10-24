import unittest

class TestStringMethods(unittest.TestCase):
	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test_isupper(self):
		self.assertFalse('foo'.isupper())
		self.assertTrue('FOO'.isupper())

	def test_split(self):
		s= 'hello world'
		self.assertEqual(s.split(),['hello','world'])
		with self.assertRaises(TypeError):
			s.split(2)

'''
if __name__=='__main__':
	unittest.main()
'''

suite= unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
