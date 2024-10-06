
#digit sum 1024 = 1 + 0 + 2 + 4 = 7

def digit_sum(num1):
    if num1 == 0:
        return 0
    else:
        return num1%10 + digit_sum(num1//10)

print(digit_sum(125), digit_sum(275))

# collatz conjective for any N: if N % 2 == 0 ; N = N/2
#                               else ; N = 3N + 1     we can always reach 1

def collatz(num1):
    if num1 == 1:
        return 0
    elif num1 % 2 == 0:
        return 1 + collatz(num1/2)
    else:
        return 1 + collatz(3 * num1 + 1)

print(collatz(4), collatz(13), collatz(25))
print(collatz(4))