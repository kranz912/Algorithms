import math
def repeatedString(s,n):
    str_len =  len(s)
    a_count = s.count('a')
    if str_len == 1 and s == 'a':
        return n
    sum_strings  = a_count*(n//str_len) + s[:n%str_len].count('a')
    counter =  0
    return sum_strings
print(repeatedString('babbaabbabaababaaabbbbbbbababbbabbbababaabbbbaaaaabbaababaaabaabbabababaabaabbbababaabbabbbababbaabb',  860622337747))
