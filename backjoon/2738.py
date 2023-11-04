N, M = map(int, input().split())
A, B = [], []

for i in range(N):
    r = list(map(int, input().split()))
    A.append(r)

for i in range(N):
    r = list(map(int, input().split()))
    B.append(r)

for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()
    

