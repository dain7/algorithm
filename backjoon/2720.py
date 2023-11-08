n = int(input())
p = [25, 10, 5, 1]

for _ in range(n):
    answer = []
    c = int(input())
    answer.append(c//p[0])
    c = c % p[0]
    answer.append(c//p[1])
    c = c % p[1]
    answer.append(c//p[2])
    c = c % p[2]
    answer.append(c//p[3]
    c = c % p[3]
    print(*answer)

