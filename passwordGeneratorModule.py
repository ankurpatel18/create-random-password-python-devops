#!/usr/local/bin/python3

import string
import random

def createNewPassword(minLen = 8, maxLen = 16):
  # add characters including letters(Uppercase and lowercase ) and digits and punctuations 
  characters = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
  # fixed size from minimum and maximm size of the randomize string
  min_max_size = random.randint(minLen, maxLen)
  # create new password from characters 
  new_password_str = ''.join(random.choice(characters) for x in range(min_max_size))
  # will check password has first character is letter, if not then it will create new password again.
  if new_password_str[0] in string.ascii_letters:
    return new_password_str
  else:
    return createNewPassword(minLen, maxLen)