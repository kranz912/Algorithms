

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dict = {}
    pairs = 0
    for i in range(n):
        dict.update({ar[i]: dict.get(ar[i])+1 if ar[i] in dict else 1})
    for key in dict:
        pairs = pairs + dict[key]//2
    return pairs
print (sockMerchant(10,[1,1,3,1,2,1,3,3,3,3]))
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = sockMerchant(n, ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
