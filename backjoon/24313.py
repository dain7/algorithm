def f(n, a1, a2):
    return n*a1 + a2

def g(c, n):
    return c*n

a1, a2 = map(int, input().split())
c = int(input())
n = int(input())

# a2가 음수인 경우에는 c가 a1보다 같거나 커야만 식이 성립한다!!
if f(n, a1, a2) <= g(c, n) and a1 <= c:
    print(1)
else:
    print(0)