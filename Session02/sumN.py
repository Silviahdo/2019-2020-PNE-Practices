# -- 1 + 1 + 2 + 3 + ... + 20
# -- 1 + ......... + 100

res20 = 0

for i in range(1, 21):
    res20 += i

res100 = 0

for i in range(1, 101):
    res100 += i

print("sum from 1-20 is:", res20)
print("sum from 1-100:", res100)

