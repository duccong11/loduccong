n = int(input("Nhập số nguyên n: "))

ket_qua = []

for i in range(1, n):
    ket_qua.append(f"{2*i} = 2*{i}")

print(", ".join(ket_qua))