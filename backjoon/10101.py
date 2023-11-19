a = int(input())
b = int(input())
c = int(input())
l = [a, b, c]
if all(i==60 for i in l):
    print("Equilateral")
elif a+b+c == 180:
    if a==b or b==c or c==a:
        print("Isosceles")
    elif a!=b and b!=c and c!=a:
        print("Scalene")
else:
    print("Error")