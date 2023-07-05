a,b = input().split()
c = bool(int(a))
d = bool(int(b))
#xor : a = true, b = false || a = false, b = true 
print((c and (not d)) or ((not c) and d))
