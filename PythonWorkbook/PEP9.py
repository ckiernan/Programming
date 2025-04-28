# -*- coding: cp1252 -*-
# PEP 9 - Pythagorean Triplet a < b < c for which a2 + b2 = c2 == 1000

# To find Pythagorean triplets, remember the rules below:
# Every odd number is the p side of a Pythagorean triplet.
# The q side of a Pythagorean triplet is simply (p2– 1)/2.
# The r side is (q2 + 1)/2.
# If p=9
# q=(92-1)/2 = (81-1)/2 = 80/2 = 40
# r=(92+1)/2 = (81+1)/2 = 82/2 = 41
# Hence, (9,40,41) are the Pythagoras triples.

a = 1

while a < 1000:
#    if a % 2 != 0:
    p = a; p2 = p^2
    q = (p^2 - 1)/2; q2 = q^2
    r = (q^2 + 1)/2; r2 = r^2
    sum = p + q; sum2 = p2 * q2
    print("p: " + str(p) + "; q: " + str(q) + "; r: " + str(r)) + "; p2: " + str(p2) + "; q2: " + str(q2) + "; r2: " + str(r2) + "; sum2: " + str(sum2)
    if sum2 > 1000: break
    a += 1
