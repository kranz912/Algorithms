'''
Challenge

You will create a function which takes a matrix filled with letters from the alphabet and determine if a 2x2 square composed of vowels exists.

If a 2x2 square of vowels is found, your function should return the top-left position (row-column) of the square.

If no 2x2 square of vowels exists, then return the string "not found".

If there are multiple squares of vowels, return the one that is at the most top-left position in the whole matrix.

Rules

Matrix must be at least 2x2
Matrix can only contain letters from the alphabet
Vowels are a e i o u.


Example

Given ["abcd", "eikr", "oufj"]

a   b   c   d
e   i   k   r
o   u   f   j
Output: [[1,0]]

'''



vowels = ['a','e','i','o','u']

def VowelSquare(arr):
    prev = arr[0]

    counter=1
    while (len(prev)<2 and counter < len(arr)):
        prev = arr[counter]
        counter +=1


    previndex = counter
    indexes = []
    for i in range(counter,len(arr)):

        consecutiveCommonVowel = 0
        for j in range(len(arr[i])):
            if arr[i][j] in vowels and prev[j] in vowels:
                consecutiveCommonVowel +=1
            else:
                consecutiveCommonVowel =0
            if consecutiveCommonVowel == 2:
                indexes.append([i-1,i])
                break

        prev = arr[i]

    return indexes


words = [
        "aaqait",
        "uakai",
        "ffoo"]


square = VowelSquare(words)

if len(square)>0:
    print(square)
else:
    print('not found')
