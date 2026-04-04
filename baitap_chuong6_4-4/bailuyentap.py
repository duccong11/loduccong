code_dict = {
    'a': '!', 'b': '@', 'c': '#', 'd': '$',
    'A': '1', 'B': '2', 'C': '3', 'D': '4'
}

# ====== HÀM MÃ HÓA ======
def encode(text):
    result = ""
    for ch in text:
        if ch in code_dict:
            result += code_dict[ch]
        else:
            result += ch   # giữ nguyên nếu không có trong bảng
    return result


# ====== HÀM GIẢI MÃ ======
def decode(text):
    # đảo ngược dictionary
    reverse_dict = {v: k for k, v in code_dict.items()}
    
    result = ""
    for ch in text:
        if ch in reverse_dict:
            result += reverse_dict[ch]
        else:
            result += ch
    return result


# ====== TEST ======
text = input("Nhập chuỗi: ")

encoded = encode(text)
decoded = decode(encoded)

print("Chuỗi mã hóa:", encoded)
print("Chuỗi giải mã:", decoded)