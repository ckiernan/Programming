# Python program to find largest palendrome for 3 digit numbers

import math

def is_palindrome(string):
  # remove any spaces and make all characters lowercase
  string = string.replace(" ", "").lower()

  # reverse the string
  reversed_string = string[::-1]

  # check if the string is equal to its reverse
  return string == reversed_string

# multiple each 3 digit numbers in decending order

a = 999
b = 999
c = 0
lrg_pal = 0

while b > 1:
    a = 999
    while a > 1:
        c = a * b
        str_c = str(c)
        print('a = ' + str(a) + '; b = ' + str(b) + '; str_c = ' + str_c)
        if is_palindrome(str_c) == True:
          print (str_c + ' is a palendrome')
          if c > lrg_pal:
            lrg_pal = c
        a -= 1
    b -= 1
print(' largest palindrome is: ' + str(lrg_pal))

# test the function
#print(is_palindrome("racecar"))  # True
#print(is_palindrome("hello"))  # False
