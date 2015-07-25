import unittest
from tests import basic


if __name__ == '__main__':
    basic_suite = unittest.TestLoader().loadTestsFromTestCase(basic.BasicTests)
    all_tests = unittest.TestSuite([basic_suite])
    unittest.TextTestRunner(verbosity=2).run(all_tests)
