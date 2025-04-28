# What is the 10001 prime number

import math
 
# A function to print all prime factors of
# a given number n

listOfPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

# Function to get sum of digits  
def getSum(n): 
   
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum

def squRootPrime(n):
    a = int(math.sqrt(n) // 1)
    print('a = ' + str(a))

    #see if the number is divisable by the primes below it
    for k in listOfPrimes
        if k % a == 0:
            return false

def primeFinder(n):

    #if its divisable by 2 is not prime
    if n % 2 ==0: return false

    # if the sum of the digits is divisable by 3 its not prime
    if getSum(n) % 3 == 0: return false

    # take squ root of number and see if any of the primes less
    # than it divide into it evenly
    

    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n // 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            print(i)
            n = n // i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)
         
# Driver Program to test above function
 
n = 315
n =  600851475143
primeFactors(n)
