lst = ['hello', 'hi', 'python', 'code', 'AI']

n = int(input("Nhập n: "))

result = []
for word in lst:
    if len(word) > n:
        result.append(word)

print(result)