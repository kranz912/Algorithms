'''
Reverse a string without affecting special characters
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.

Examples:

Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.
Only subsequence "abc" is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"
'''


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
