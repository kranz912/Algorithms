
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
