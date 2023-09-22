def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]: # 뒤에서 거꾸로 4개가 해당 리스트와 같은 경우
            cnt += 1 # 햄버거 하나 만들어주고
            for _ in range(4): # 뒤에서부터 하나씩 삭제
                s.pop()
    return cnt