H, M = map(int, input().split())
total = H * 60 + M - 45 
if total < 0 :
    total += 60 *24
H = total // 60
M = total % 60
print(H, M)