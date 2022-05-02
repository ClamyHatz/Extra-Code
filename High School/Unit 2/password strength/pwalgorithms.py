# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("D:/CSP/password strength/dictionary.txt")
  for line in dictionary_file:
    # store word, ommitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    for e in words:
      guesses += 1
      if (w+e == password):
        return True, guesses
  return False, guesses

def two_words_and_a_diget(password):
  words = get_dictionary()
  guesses = 0
  digets = "0123456789"
  # get each word from the dictionary file
  for w in words:
    for e in words:
      for d in digets:
        guesses += 1
        if (w+e+d == password) or (d+w+e == password):
          return True, guesses
  return False, guesses


def two_words_a_diget_and_a_symbol(password):
  words = get_dictionary()
  guesses = 0
  digets = "0123456789"
  symbols = "~!@#$%^&*()_-+={[}]|\:<>."
  # get each word from the dictionary file
  for w in words:
    for e in words:
      for d in digets:
        guesses += 1
        if  or (d+w+e == password):
          return True, guesses
  return False, guesses