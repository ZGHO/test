# import unittest
# from module import Caculator
#
#
# class ModelTest(unittest.TestCase):
#
#     def setUp(self):
#         self.cal = Caculator(8, 4)
#
#     def tearDown(self):
#         pass
#
#     def test_add(self):
#         result = self.cal.add()
#         self.assertEqual(result, 12)
#
#     def test_sub(self):
#         result = self.cal.sub()
#         self.assertEqual(result, 4)
#
#     def test_mul(self):
#         result = self.cal.mul()
#         self.assertEqual(result, 32)
#
#     def test_div(self):
#         result = self.cal.div()
#         self.assertEqual(result, 2)
#
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(ModelTest("test_add"))
#     suite.addTest(ModelTest("test_sub"))
#     suite.addTest(ModelTest("test_mul"))
#     suite.addTest(ModelTest("test_div"))
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
