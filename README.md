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


### 3. Reverse a string without affecting special characters
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.

```
Examples:

Input:   str = "a,b$c"
Output:  str = "c,b$a"
#Note that $ and , are not moved anywhere.  
#Only subsequence "abc" is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"
```
