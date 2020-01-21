
vowels = ['a','e','i','o','u']

def VowelSquare(arr):
    prev = arr[0]

    counter=1
    while (len(prev)<2 and counter < len(arr)):
        prev = arr[counter]
        counter +=1


    previndex = counter
    indexes = []
    for i in range(counter,len(arr)):

        consecutiveCommonVowel = 0
        for j in range(len(arr[i])):
            if arr[i][j] in vowels and prev[j] in vowels:
                consecutiveCommonVowel +=1
            else:
                consecutiveCommonVowel =0
            if consecutiveCommonVowel == 2:
                indexes.append([i-1,i])
                break

        prev = arr[i]

    return indexes


words = [
        "aaqait",
        "uakai",
        "ffoo"]


square = VowelSquare(words)

if len(square)>0:

    print(square)
else:
    print('not found')
