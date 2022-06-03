def palindrome(word):
  word = word.lower()
  return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Mom"))

# Apparetnly this [::-1] reverses an iterable.
# def rev(word):
#   return word[::-1]

# print(rev("silly"))