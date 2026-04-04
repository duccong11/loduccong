lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = []
odd = []

for x in lst:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Số chẵn:", even)
print("Số lẻ:", odd)