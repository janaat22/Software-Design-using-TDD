import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src'))

from applicant.applicant import Applicant

class ApplicantStatusTest():
  def test_applicant_status(self):
    applicant = Applicant()
    
    self.assertEqual(self.expected_status(), self.check(applicant))
