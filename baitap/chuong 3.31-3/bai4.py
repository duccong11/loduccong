n = int(input("Nhập vào 1 số nguyên n (n < 20): "))

if n >= 20:
    print("Vui lòng nhập n nhỏ hơn 20 theo đúng yêu cầu đề bài!")
else:
    print(f"Các số từ 1 đến {n} chia hết cho 5 hoặc 7 là:", end=" ")
    
    tim_thay = False 
    
    for i in range(1, n + 1):
        if i % 5 == 0 or i % 7 == 0:
            print(i, end=" ")
            tim_thay = True 
            
    if tim_thay == False:
        print("Không có số nào!")
    else:
        print()