def find_lcm_of_three_numbers(a, b, c):
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)

    lcm_ab = lcm(a, b)
    lcm_abc = lcm(lcm_ab, c)

    multiples = set()
    i = 0
    while i <= 1000:
        multiples.add(i)
        i += lcm_abc

    return multiples

a = 18
b = 24
c = 40

result = find_lcm_of_three_numbers(a, b, c)
print(result)
