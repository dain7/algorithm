N, M = map(int, input().split())
l = [i+1 for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    temp = l[a-1]
    l[a-1] = l[b-1]
    l[b-1] = temp

print(*l)