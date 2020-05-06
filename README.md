# Algorithms

### 1. DI String Match

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

```
If S[i] == "I", then A[i] < A[i+1]

If S[i] == "D", then A[i] > A[i+1]
```

Example 1:
```
Input: "IDID"
Output: [0,4,1,3,2]
```
Example 2:
```
Input: "III"
Output: [0,1,2,3]
```
Example 3:

Input: "DDI"
Output: [3,2,0,1]


Note:
1. <= S.length <= 10000
2. S only contains characters "I" or "D".

#### Solution:
```python
S = "IDID"
N = len(S)
A = [x for x in range(N+1)]
B= []

for i in range(len(S)):
    if S[i]=='I':
        B.append(A.pop(0))
    else:
        B.append(A.pop())

B.append(A.pop())
print(B)

```

### 2. Vowel Square

You will create a function which takes a matrix filled with letters from the alphabet and determine if a 2x2 square composed of vowels exists.

If a 2x2 square of vowels is found, your function should return the top-left position (row-column) of the square.

If no 2x2 square of vowels exists, then return the string "not found".

If there are multiple squares of vowels, return the one that is at the most top-left position in the whole matrix.

Rules

1. Matrix must be at least 2x2
2. Matrix can only contain letters from the alphabet
3. Vowels are a e i o u.

```
Example
Input ["abcd", "eikr", "oufj"]
Output: [[1,0]]
```

#### Solution:
```python
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

```


### 3. Reverse a string without affecting special characters
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.

```
Examples:

Input: "a,b$c"
Output: "c,b$a"
#Note that $ and , are not moved anywhere.  
#Only subsequence "abc" is reversed

Input:  "Ab,c,de!$"
Output: "ed,c,bA!$"
```


#### Solution:
```python
def reverseString(text):
    r=len(text)-1
    l=0
    x=[]

    while len(x) != len(text):
        right = text[r]
        left  = text[l]
        if(not left.isalpha()):
            x.append(left)
        else:
            while True:
                r=r-1
                if right.isalpha():
                    x.append(right)
                    break
                right = text[r]
        l=l+1
    return "".join(x)

print(reverseString("a!!!b.c.d,e'f,ghi"))
```

### 4. Remove duplicates from a give string
Given a string S, the task is to remove all the duplicates in the given string.
```
Examples:

Input: aaasbb
Output: asb

```

#### Solution:
```python
def removeDuplicates(S):
    dict = {}
    for s in S:
        dict.update({s:1})
    return "".join(dict.keys())

print(removeDuplicates("aaasbb"))
```

### 5. Check Pangram
Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.
```
Examples:

"The quick brown fox jumps over the lazy dog" is a Pangram [Contains all the characters from 'a' to 'z']
"The quick brown fox jumps over the dog" is not a Pangram [Doesn't contains all the characters from 'a' to 'z', as 'l', 'z', 'y' are missing]
```

#### Solution:
```python

def checkPangram(S):
    dict = {}
    S= S.lower()
    for s in S:
        if s.isalpha():
            dict.update({s:1})
    return len(dict) ==26

print(checkPangram("The quick brown fox jumps over the lazy dog"))

```


### 6. Check Pangram Missing Characters
Pangram is a sentence containing every letter in the English alphabet. Given a string, find all characters that are missing from the string, i.e., the characters that can make string a Pangram. We need to print output in alphabetic order.

```
Examples:

Input : welcome to geeksforgeeks
Output : abdhijnpquvxyz

Input : The quick brown fox jumps
Output : adglvyz
```



#### Solution
``` python
def checkPangram(S):
    dict = {}
    S= S.lower()
    for s in S:
        if s.isalpha():
            dict.update({s:1})
    return len(dict) ==26

print(checkPangram("The quick brown fox jumps over the lazy dog"))

```
