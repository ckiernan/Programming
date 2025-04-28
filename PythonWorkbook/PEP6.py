# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

import math

a = 100
sum_of_squares = 0
sum_squared_squared = 0

for x in range(1,a + 1):
    sum_of_squares = sum_of_squares + (x * x)
    print('Sum of Squares = ' + str(sum_of_squares))
for y in range(1, a + 1):
    sum_squared_squared = sum_squared_squared + y
    print('Sum Squared = ' + str(sum_squared_squared))
sum_squared_squared = pow(sum_squared_squared,2)

print('Solution = ' + str(sum_squared_squared - sum_of_squares))
    
