info = {
    "ten": input("Tên: "),
    "tuoi": input("Tuổi: "),
    "email": input("Email: "),
    "skype": input("Skype: "),
    "dia_chi": input("Địa chỉ: "),
    "noi_lam_viec": input("Nơi làm việc: ")
}

# Ghi file
with open("setInfo.txt", "w", encoding="utf-8") as f:
    for k, v in info.items():
        f.write(f"{k}:{v}\n")

# Đọc file
print("\nDữ liệu đã lưu:")
with open("setInfo.txt", "r", encoding="utf-8") as f:
    print(f.read())