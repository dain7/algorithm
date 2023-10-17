H, M = map(int, input().split())

N = int(input())

s = H * 60 + M + N
H = s//60
M = s%60

if H >= 24:
    H = H%24

print(H, M)



##### 다른사람 풀이 
print((h+(m+c)//60)%24, (m+c)%60)