H, M = map(int, input().split())
total = H * 60 + M - 45  # 분으로 만들어준다.
if total < 0 : 
    total += 60 *24 # 24시간,,을 분으로 만들어준다.
H = total // 60 # 몫
M = total % 60 # 나머지
print(H, M)