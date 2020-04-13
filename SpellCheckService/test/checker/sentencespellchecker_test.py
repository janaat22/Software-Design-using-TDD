import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src/checker'))
sys.path.insert(0,os.path.join('C:/Users/janaa/OneDrive/Desktop/Sem3/SD/HW/vijayakumar_zaman/assign2/src/checker'))

from sentencespellchecker import SentenceSpellChecker

class SentenceSpellCheckerTest(unittest.TestCase):
  def setUp(self):
    self.sentence_spell_checker = SentenceSpellChecker()
  
  def test_canary(self):
    self.assertTrue(True)
  
  def test_check_spelling_empty_string(self):
    self.assertEqual(self.sentence_spell_checker.check_spelling(""), "")
  
  def test_check_spelling_one_correct_word(self):
    self.assertEqual(self.sentence_spell_checker.check_spelling("one"), "one")
  
  def test_check_spelling_two_correct_words(self):
    self.assertEqual(
      self.sentence_spell_checker.check_spelling("two words"), "two words")
  
  def test_check_spelling_one_incorrect_word(self):
    self.assertEqual(
      self.sentence_spell_checker.check_spelling("oen", lambda word: False),
      "[oen]")
  
  def test_check_spelling_correct_word_following_incorrect_word(self):
    self.assertEqual(self.sentence_spell_checker.check_spelling("oen two",
      lambda word: word != "oen"), "[oen] two")
  
  def test_check_spelling_incorrect_word_following_correct_word(self):
    self.assertEqual(self.sentence_spell_checker.check_spelling("one wto",
      lambda word: word != "wto"), "one [wto]")
  
  def test_check_spelling_two_incorrect_words(self):
    self.assertEqual(self.sentence_spell_checker.check_spelling("oen wto",
      lambda word: False), "[oen] [wto]")
  
  def test_check_spelling_when_there_is_an_error(self):
    def throw(ex): raise ex
    
    with self.assertRaises(Exception) as ex:
      self.sentence_spell_checker.check_spelling("one",
        lambda word: throw(Exception('oops, unable to check spelling!!')))
    
    self.assertEqual('oops, unable to check spelling!!', str(ex.exception))

if __name__ == '__main__':
  unittest.main()
