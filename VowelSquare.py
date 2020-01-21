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
            if len(matrix)>2:
                squence = []
    matrix2.append(squence)
print(matrix2)
