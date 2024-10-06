# numbers factorial 6! = 6*5*4*3*2*1= 720

def fact(num1):
    if num1 == 1:
        return 1
    else:
        return num1 * fact(num1-1)

# fiboncci seq 0,1,1,2,3,5,8,13,21,34,55,88,144...

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib( n -2)



print('3! =', fact(3))
print('6! =', fact(6))


print('5th fibonacci number:', fib(5))
print('7th fibonnaci number:', fib(7))

