original = [1, 1, 2, 2, 2, 8]
answer = []
dong = list(map(int, input().split()))

for i in range(len(original)):
    answer.append(original[i]-dong[i])

print(*answer)