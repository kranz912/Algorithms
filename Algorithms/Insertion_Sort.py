def Insertion_Sort(A):
    ''' Implementation of Insertion_Sort
        INPUT   :   An array of integers [a1,a2,a3,a4,a5,...an]
        OUTPUT  :   An array of sorted integers a1 <= ai <= an

    '''
    n = len(A)
    for j in range(1,n):
        key = A[j]
        i = j-1
        while i>=0 and A[i]<key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A
print(Insertion_Sort([2,3,1,3,1,5]))
