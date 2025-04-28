x = 0; y = 1; z = 0
sum = 0
fib_seq = [2]

while z <= 4000000:
    z = x + y
    if z % 2 == 0:
        fib_seq.append(z)
        sum = sum + z
        print('the Fib Squence is ', fib_seq)
        print('Sum of Fib Seq is ',sum)
    x = y
    y = z
    
