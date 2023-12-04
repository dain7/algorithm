# 중복없이 n개 중 r개를 뽑는다.
n = int(input())
answer = n*(n-1)*(n-2)/6
print("""%i
3""" % answer)