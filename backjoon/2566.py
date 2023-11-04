A =[]

for i in range(9):
    row = list(map(int, input().split()))
    A.append(row)

m = 0
r = 0
c = 0
for i in range(9):
    for j in range(9):
        if A[i][j] > m:
            m = A[i][j]
            r = i
            c = j

print(m)
print(r+1, c+1)