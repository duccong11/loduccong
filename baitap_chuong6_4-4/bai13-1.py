# Khai báo tuple ban đầu
my_tuple = ('a', 'b', 'd', 'e')

# Chuyển tuple sang list để có thể thay đổi
temp_list = list(my_tuple)

# Thêm phần tử 'c' vào vị trí index 2
temp_list.insert(2, 'c')

# Chuyển lại thành tuple
new_tuple = tuple(temp_list)

# In kết quả
print("Tuple ban đầu:", my_tuple)
print("Tuple sau khi thêm:", new_tuple)