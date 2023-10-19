l = [i for i in range(1, 31)]

for _ in range(28):
    l.remove(int(input()))

print(min(l))
print(max(l))


### 외계어..?
print(*{*map(int,open(0))}^{*range(1,31)})
