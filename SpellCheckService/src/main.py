import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'checker'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'reader'))

from sentencereader import read_sentences
from sentencespellchecker import SentenceSpellChecker
from spellcheckerservice import check_spelling

if __name__ == '__main__':
  sentencespellchecker = SentenceSpellChecker()
  try:
    print("".join(map(
      lambda sentence: sentencespellchecker.check_spelling(
        sentence, lambda word: check_spelling(word)), read_sentences())))
  except:
    print('The service is unavailable due to %s' % sys.exc_info()[0].__name__)
