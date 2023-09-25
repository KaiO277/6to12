'''
Để giải quyết bài toán trên chúng ta sẽ giải như sau:
 B1: Chúng ta sẽ khỏi tạo một vòng lặp (`for`,`while`,...)
 B2: Sử dụng câu điều kiện để kiểm tra lại yêu cầu bài toán đưa ra.
 B3: In ra những số thoả điều kiện.
'''

n = 1000 # Vì n là tập hợp số tự nhiên ta gán n=1000 có thể lớn hơn
A = set()

for x in range(n+1):
    if x < 5:
        A.add(x)

print(f'A={A}')