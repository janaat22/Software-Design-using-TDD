class FactorialTests():
  def test_canary(self):
    self.assertTrue(True)
  
  def test_for_zero_returns_one(self):
    self.assertEqual(1, self.factorial(0))
  
  def test_for_one_returns_one(self):
    self.assertEqual(1, self.factorial(1))
  
  def test_for_two_returns_two(self):
    self.assertEqual(2, self.factorial(2))
  
  def test_for_three_returns_six(self):
    self.assertEqual(6, self.factorial(3))
  
  def test_factorial_for_ten(self):
    self.assertEqual(3628800, self.factorial(10))
  
  def test_factorial_for_fifty(self):
    self.assertEqual(
      30414093201713378043612608166064768844377641568960512000000000000,
      self.factorial(50))
  
  def test_factorial_for_negative_number(self):
    self.assertRaisesRegex(Exception,
      'Undefined for invalid input!',
      self.factorial,
      -1)
