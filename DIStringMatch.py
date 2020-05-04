'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]

Example 2:

Input: "III"
Output: [0,1,2,3]


Example 3:

Input: "DDI"
Output: [3,2,0,1]

'''


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
