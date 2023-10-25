# 진수를 구할 때
# 자릿수 * 2**0 , 자릿수 * 2**1 ... 그런데 한자릿수부터 n승이 0, 1부터 시작.
# N을 뒤집어서 0승부터 계산..
N, B = input().split(" ")
B = int(B)
d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = 0
for i, num in enumerate(N[::-1]):
    answer += d.index(num) * B ** i

print(answer)



###### 

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
answer = 0
for i, num in enumerate(n[::-1]):
    answer += int(b) ** i * num_list.index(num)
print(answer)