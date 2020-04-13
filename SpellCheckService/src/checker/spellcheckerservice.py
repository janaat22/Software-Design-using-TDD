from urllib import request

def check_spelling(word,
  get_data = lambda word:
  request.urlopen("http://agile.cs.uh.edu/spell?check=%s" % word).read()):
  return get_data(word).decode("utf-8") == 'true'
