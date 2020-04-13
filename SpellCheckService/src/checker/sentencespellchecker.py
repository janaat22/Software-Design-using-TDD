class SentenceSpellChecker():
  def check_spelling(self, sentence, spell_checker = lambda word: True):
    return " ".join(
      map(lambda word: word if spell_checker(word) else "[" + word + "]",
        sentence.split(" ")))
