import math

def lcm(a, b):
    # Tính GCD của a và b
    gcd = math.gcd(a, b)
    
    # Tính LCM bằng công thức LCM = (a * b) / GCD
    lcm = (a * b) // gcd
    
    return lcm

# Đầu vào
a = 12
b = 18

# Tìm LCM của a và b
result = lcm(a, b)

# In kết quả
print(f"LCM của {a} và {b} là {result}")
