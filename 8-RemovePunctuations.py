'''
Removing punctuations from a given string

Given a string, remove the punctuation from the string if the given character is a punctuation character as classified by the current C locale. The default C locale classifies these characters as punctuation:

!"#$%&'()*+,-./:;?@[\]^_`{|}~
Examples:

Input : %welcome' to @geeksforgeek<s
Output : welcome to geeksforgeeks

Input : Hello!!!, he said ---and went.
Output : Hello he said and went


'''

punctuations = '''!"#$%&'()*+,-./:;?@[\]^_`{|}~<>'''

def removePunctuations(S):
    for p in punctuations:
        S =  S.replace(p,'')
    return S

print(removePunctuations('''%welcome' to @geeksforgeek<s'''))
