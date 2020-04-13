import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src'))

from evaluate.employment_check import check
from utilities.evaluation_result import EvaluationResult
from applicant_status_test import ApplicantStatusTest

class CheckEmploymentTest(ApplicantStatusTest, unittest.TestCase):
  def expected_status(self):
    return (EvaluationResult.PASS, "Applicant has previous employment")
  
  def check(self, applicant):
    return check(applicant)
