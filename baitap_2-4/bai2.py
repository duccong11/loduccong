text = input("Nhập đoạn văn: ")

# Ghi file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Đọc file
with open("output.txt", "r", encoding="utf-8") as f:
    print("Nội dung file:", f.read())