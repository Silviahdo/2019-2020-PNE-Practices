# Create a file with the fibonacci numbers
count = 0
n1 = 0
n2 = 1
for i in range(0, 11):
    print(n1, end=' ')
    n = n1 + n2
    n1 = n2
    n2 = n
    count += i


