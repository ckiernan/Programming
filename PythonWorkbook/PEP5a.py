

# Python program which check is a number
# divided with every element in list
# or not
def findNoIsDivisibleOrNot(n, l =[]):
 
    # Checking if a number is divided
    # by every element or not
    for i in range(0, len(l)):
        print('l['+ str(i) +'] = ' + str(l[i]))
        if l[i]% n != 0:
            return 0
    return 1
 
# Driver code
a = 21
k = False

while k == False:
    l = [1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#    l.append(a)
    l.append(2600)
    print('l = ' + str(l))
    n = 1
    if findNoIsDivisibleOrNot(n, l) == 1:
          print ("Yes")
          k = True
          break
    else:
          print ("No")
          k = False
          a =+ 1
