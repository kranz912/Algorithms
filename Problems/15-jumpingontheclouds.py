def jumpingOnClouds(c):
    n = len(c) -1
    jumps = 0
    consecutive = 0

    for i in range(n):
        if c[i] == 0:
            consecutive = consecutive +1
            if consecutive == 2:
                consecutive = 0
                jumps = jumps +1
        if c[i] == 1:
            jumps = jumps +1
            consecutive = 0
    jumps =  jumps + consecutive
    return jumps
