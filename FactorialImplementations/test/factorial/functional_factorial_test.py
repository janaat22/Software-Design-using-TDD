import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src/factorial'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'test/factorial'))

from factorial_tests import FactorialTests
from functional_factorial import factorial

class TestFunctionalFactorial(FactorialTests, unittest.TestCase):
  def factorial(self, number):
    return factorial(number)
