'''
Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.

Examples :
 "The quick brown fox jumps over the lazy dog" is a Pangram [Contains all the characters from 'a' to 'z']
"The quick brown fox jumps over the dog" is not a Pangram [Doesn't contains all the characters from 'a' to 'z', as 'l', 'z', 'y' are missing]
'''


def checkPangram(S):
    dict = {}
    S= S.lower()
    for s in S:
        if s.isalpha():
            dict.update({s:1})
    return len(dict) ==26

print(checkPangram("The quick brown fox jumps over the lazy dog"))
