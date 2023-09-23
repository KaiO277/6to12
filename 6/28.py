import math

def lcm(a, b):
    # Tính GCD của a và b
    gcd = math.gcd(a, b)
    
    # Tính LCM bằng công thức LCM = (a * b) / GCD
    lcm = (a * b) // gcd
    
    return lcm

def lcm_of_three(a, b, c):
    # Tính LCM của a và b
    lcm_ab = lcm(a, b)
    
    # Tính LCM của lcm_ab và c
    lcm_abc = lcm(lcm_ab, c)
    
    return lcm_abc

# Đầu vào
a = 8
b = 9
c = 72

# Tìm LCM của a, b và c
result = lcm_of_three(a, b, c)

# In kết quả
print(f"LCM của {a}, {b} và {c} là {result}")
