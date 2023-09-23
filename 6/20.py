from itertools import permutations

# Tạo tất cả các hoán vị của 3 số
numbers = [3, 0, 4]
permutations_list = permutations(numbers)

# Danh sách các số thoả mãn điều kiện
result_list = []

for perm in permutations_list:
    number = int("".join(map(str, perm)))  # Chuyển hoán vị thành số nguyên
    if number % 2 == 0 and number > 99:  # Kiểm tra điều kiện
        result_list.append(number)

# In danh sách các số thoả mãn
print("Danh sách các số thoả mãn điều kiện:")
for number in result_list:
    print(number)
