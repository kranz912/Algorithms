'''
Pangram is a sentence containing every letter in the English alphabet. Given a string, find all characters that are missing from the string, i.e., the characters that can make string a Pangram. We need to print output in alphabetic order.

Examples:

Input : welcome to geeksforgeeks
Output : abdhijnpquvxyz

Input : The quick brown fox jumps
Output : adglvyz
'''

letter = 'a'
alphabet = []


for index in range(0,26):
    alphabet.append(letter)
    letter = chr(ord(letter)+1)


def CheckMissingCharacters(S):
    S = S.lower()
    for s in S:
        if s.isalpha():
            if s in alphabet:
                alphabet.remove(s)

    return "".join(alphabet)

print(CheckMissingCharacters("The quick brown fox jumps over the lazy do"))
