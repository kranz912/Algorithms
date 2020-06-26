

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    index = 0

    while index < n:
        level =  1 if s[index] == 'U' else -1
        index = index +1
        if level < 0:
            valleys = valleys +1
        while level != 0:
            if s[index] == 'U':
                level=level +1
            elif s[index]== 'D':
                level=level-1
            index = index +1
    return valleys

n =  12
s = 'DDUUDDUDUUUD'
print(countingValleys(n,s))
