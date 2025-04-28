x = 0
y = 0
while x < 1000:
    print (x)
    if x % 3 == 0:
        print (str(x) + ' is a muliple of 3')
        y = y + x

    elif x % 5 == 0:
        print (str(x) + ' is a muliple of 5')
        y = y + x
    x = x + 1
print('The sum of all mulitples of 3 and 5 are: ' + str(y))
