def checkIfNumerIsPalindrome(x):
    ispalindrome = True
    i = 0
    x = str(x)
    while((i<len(x)/2) and ispalindrome):
        if(x[i] != x[-(i+1)]):
            ispalindrome = False
        i+=1
    return ispalindrome

print(checkIfNumerIsPalindrome(10000))

pals = []

for x in range(10000,100000):
    if(checkIfNumerIsPalindrome(x)):
        pals.append(x)

print(len(pals))


even_pals = []
for x in pals:
    if x%2 == 0:
        even_pals.append(x)

print(len(even_pals))



seven_eight_pals = []

for x in pals:
    for y in str(x):
        if (y=='7' or y=='8'):
            seven_eight_pals.append(x)
            break
print(len(seven_eight_pals))
