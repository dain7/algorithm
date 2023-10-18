N = int(input())

for _ in range(N//4) :
    print("long", end="\n")
print("int")


##### python magic
print(int(input())//4*'long '+'int')