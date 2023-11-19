a, b, c = map(int, input().split())
m = max((a,b,c))
if sum((a,b,c))-m > m:
    print(sum((a,b,c)))
else:
    min_m = sum((a,b,c))-m-1
    print(sum((a,b,c))-m + min_m)