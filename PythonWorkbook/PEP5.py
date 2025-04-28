#PEP5 - 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

sum_a = 0
sum_b = 0

#sum_a = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20
sum_a = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
print('sum_a = ' + str(sum_a))

sum_b = 1 * 2 * 3 * 4 * 5 * 6
print('sum_b = ' + str(sum_b))

lrg_factor = sum_a /1440

print('lrg_factor = ' + str(lrg_factor))
