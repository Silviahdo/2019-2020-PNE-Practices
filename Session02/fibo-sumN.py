#Session 2. Exercise 3

def sumn(n):
    count = 0
    res = 0
    n1 = 0
    n2 = 1
    for i in range(0, n+1):
        if i == 0:
            count = 0
        elif i == 1:
            res = res + 1
        else:
            count = n1 + n2
            n1 = n2
            n2 = count
            res = res + count
    return res

print("sum of 1-5: ", sumn(5))
print("sum from 1-10: ", sumn(10))
