#Exercise 2

count_A = 0
count_C = 0
count_T = 0
count_G = 0

seq_dna = input("Introduce the sequence: ")

for i in seq_dna:
    if i == "A":
        count_A += 1
    elif i == "C":
        count_C += 1
    elif i == "T":
        count_T += 1
    elif i == "G":
        count_G += 1

print("Total length: ", len(seq_dna))
print("A:", count_A)
print("C:", count_C)
print("T:", count_T)
print("G:", count_G)
