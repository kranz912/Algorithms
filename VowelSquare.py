arr = ["aqrst", "ukaei", "ffooo"]
vowels = ['a','e','i','o','u']
matrix = []
for words in arr:
    vector = []
    for letter in words:
        vector.append(letter in vowels)
    matrix.append(vector)


matrix2 = []
for i in range(len(matrix)):
    squence= []
    for j in range(len(matrix[i])):
        if matrix[i][j]:
            squence.append(j)
        else:
            if len(squence)>2:
                squence = []
    matrix2.append(squence)
print(matrix2)

prev = matrix2[0]

for x in range(1,len(matrix2)):
    sq = []
    for y in matrix2[x]:
        if y in prev:
            sq.append(y)
        else:
