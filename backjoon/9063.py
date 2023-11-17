# 시간 에바쎼바
n = int(input())

min_x = 99999
min_y = 99999
max_x = -99999
max_y = -99999

for _ in range(n):
    x, y = map(int, input().split())
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

print((max_x-min_x)*(max_y-min_y))


# 시간 훨씬 빠름 ...
N, *cases = map(int, open(0).read().split())
x_list = cases[::2]
y_list = cases[1::2]

answer = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))
print(answer)