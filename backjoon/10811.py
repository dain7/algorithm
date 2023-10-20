N, M = map(int, input().split())
l = [i for i in range(1, N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    temp = l[a-1:b]
    temp.reverse()
    l[a-1:b] = temp
print(*l)
