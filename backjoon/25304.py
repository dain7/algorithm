X = int(input())
N = int(input())
answer = 0

for _ in range(N):
    a, b = map(int, input().split())
    answer += a * b

print("Yes" if answer == X else "No")