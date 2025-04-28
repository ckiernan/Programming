#Calculate Pythagorean Triplet where a2 * b2 = c2 where c2 = 1000

# to find pythag triplet for starting wtih a given even number use:
# 2m^2 + (m^2 - 1)^2 = (m^2 + 1)^2
# 

# for even a given odd number use:
# take the odd number and divide it by 2, that's the 2nd number, add 1 to it for the 3rd number

import math

a = 0, b = 0, c = 0, a2 = 0, b2 = 0, c2 = 0, m = 0

try:

while c2 < 1001

	If m % 2 = 0: # even number
		b = m / 2, c = b + 1
		a2 = m^2, b2 = b^2, c2 = (m + b)^2
		Print('Even, a: ' %s ', b: '%s ', c: ' %s , 'a2 + b2 = c2: ' %s, (m , b, c, c2)) 
	else: #odd number
		a = m / 2, a2 = a^2
		b2 = (a2 - 1)^2, b = math.sqrt(b2)
		c2 = (a2 - 1)^2, c = math.sqrt(c2)
		Print('Odd, a: ' %s ', b: '%s ', c: ' %s , 'a2 + b2 = c2: ' %s, (m , b, c, c2)) 
		
		
