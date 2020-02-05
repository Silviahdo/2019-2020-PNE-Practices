# Sesion 2. Exercise 2

def fibon(n):
    n1 = 0
    n2 = 1
    counter = 0
    for number in range(0, n+1):
        if number == 0:
            counter = 0
        elif number == 1:
            counter = 1
        else:
            counter = n1 + n2
            n1 = n2
            n2 = counter
    return counter

print("The 5th term of the fibonacci serie is:", fibon(5))
print("The 10th term of the fibonacci serie is:", fibon(10))
print("The 15th term of the fibonacci serie is:", fibon(15))
