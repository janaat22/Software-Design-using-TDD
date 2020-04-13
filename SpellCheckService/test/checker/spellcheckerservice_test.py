import os, sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src/checker'))
sys.path.insert(0,os.path.join('C:/Users/janaa/OneDrive/Desktop/Sem3/SD/HW/vijayakumar_zaman/assign2/src/checker'))

from spellcheckerservice import check_spelling

class SentenceSpellCheckerServiceTest(unittest.TestCase):
  def test_spell_check_for_correct_word(self):
    self.assertTrue(check_spelling('one'))
  
  def test_spell_check_for_incorrect_word(self):
    self.assertFalse(check_spelling('brke'))
  
  def test_spell_check_when_network_error(self):
    def throw(ex): raise ex
    
    with self.assertRaises(Exception):
      check_spelling("one", lambda word: throw(Exception))

if __name__ == '__main__':
  unittest.main()
