# 내 답
while True:
    n = int(input())
    if n == -1:
        break

    l = []
    for i in range(1, n//2+1):
        if n%i == 0:
            l.append(i)
    if n != sum(l):
        print(str(n)+" is NOT perfect.")
    else:
        a = str(n) + " = "
        for i in l:
            a += str(i)
            if i != l[-1]:
                a += " + "
        print(a)

# 다른사람 풀이
while 1:
    n=int(input())
    if n==-1:break
    end=int(n**(1/2))
    l=[]
    for i in range(2,end+1):
        if n%i==0:
            l.extend((i,n//i))
    l.append(1)
    if sum(l)==n:
        l.sort()
        print(n,'=',end=' ') # 이 부분이
        print(*l,sep=' + ')  # 좋군요
    else:print(f'{n} is NOT perfect.')