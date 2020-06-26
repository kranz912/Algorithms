'''
Rearrange characters in a string such that no two adjacent are same
Given a string with repeated characters, the task is to rearrange characters in a string so that no two adjacent characters are same.

Note : It may be assumed that the string has only lowercase English alphabets.

Examples:



Input: aaabc
Output: abaca

Input: aaabb
Output: ababa

Input: aa
Output: Not Possible

Input: aaaabc
Output: Not Possible
'''


def rearrangeChar(S):
    l =  list(S)
    queue = []
    str = []
    while len(l)>0:
        last_index = len(str)-1
        s = l.pop(0)
        if last_index != -1:
            if str[last_index] != s:
                str.append(s)
                while len(queue)>0:
                    l.insert(0,queue.pop(0))
            else:
                queue.append(s)
        else:
            str.append(s)
    if len(str) != len(S):
        return 'Not Possible'
    return "".join(str)

print(rearrangeChar('bbbaa'))
