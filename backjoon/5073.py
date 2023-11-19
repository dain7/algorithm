while True:
    a, b, c = map(int, input().split())

    if a == b == c== 0:
        break
    # sum에는 두가지 변수 안되니께 한번 더 묶어주슈
    if sum((a,b,c)) - max((a,b,c)) <= max((a,b,c)):
        print("Invalid")
    elif a== b == c:
        print("Equilateral")
    elif a == b or b == c or a == c :
        print("Isosceles")
    else:
        print("Scalene")
