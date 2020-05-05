'''
Remove duplicates from a give string

Given a string S, the task is to remove all the duplicates in the given string.

Example:

Input: "aaasbb"
Output: "asb"

'''



def removeDuplicates(S):
    dict = {}
    for s in S:
        dict.update({s:1})
    return "".join(dict.keys())

print(removeDuplicates("aaasbb"))
