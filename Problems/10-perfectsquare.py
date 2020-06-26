import math
arr = []
for x in range(1,101):
    root = math.sqrt(x)
    if int(root+0.5)** 2 == x:
        arr.append(x)
print(len(arr))
