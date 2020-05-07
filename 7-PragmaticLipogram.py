# -*- coding: utf-8 -*-
'''
Check if a string is Pangrammatic Lipogram
To understand what a pangrammatic lipogram is we will break this term down into 2 terms i.e. a pangram and a lipogram

Pangram: A pangram or holoalphabetic sentence is a sentence using every letter of a given alphabet at least once. The best-known English pangram is 'The quick brown fox jumps over the lazy dog.'

Lipogram: A lipogram is a kind of constrained writing or word game consisting of writing paragraphs or longer works in which a particular letter or group of letters is avoided—usually a common vowel, and frequently E, the most common letter in the English language.
Example: The original 'Mary Had a Little Lamb' was changed by A. Ross Eckler Jr. to exclude the letter 'S'.

'''


def checkIfPragmaticLipogram(S):
    dict = {}
    S = S.lower()
    for s in S:
        if s.isalpha():
            dict.update({s:1})
    return len(dict)==25

print(checkIfPragmaticLipogram("The quick brown fox jumps over the lay do"))
