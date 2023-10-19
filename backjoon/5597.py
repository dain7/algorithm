l = [i for i in range(1, 31)]

for _ in range(28):
    l.remove(int(input()))

print(min(l))
print(max(l))


### 외계어..?
print(*{*map(int,open(0))}^{*range(1,31)})

{*map(int, open(0))} # {1,2,3,.., 30} set 중 두개가 빠진 set
{*range(1,31)} # {1,2,..30} set
^ # 교집합 제거 연산
# {4,28}을 *로 풀어서