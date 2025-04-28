

# Python program which check is a number
# divided with every element in list
# or not
def findNoIsDivisibleOrNot(n, l=[]):
 
    # Checking if a number is divided
    # by every element or not
    for i in range(0, len(l)):
        if n % l[i] != 0:
            #print('Not Equ; l['+ str(i) +'] = ' + str(l[i]))
            return 0
    return 1
 
# Driver code
a = 21
k = False

l = [1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#l = [1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10]

while k == False:
#while a < 2525:
#    print('a = ' + str(a))
#    print('l = ' + str(l))
    if findNoIsDivisibleOrNot(a, l) == 1:
        print ("Yes, the answer is: " + str(a))
        k = True
        a = a + 1
    else:
         # print ("No")
          k = False
          a = a + 1
