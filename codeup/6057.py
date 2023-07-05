a,b = input().split()
c = bool(int(a))
d = bool(int(b))
#xor : a = true, b = false || a = false, b = true 
print(c and d or ((not c) and (not d)))
