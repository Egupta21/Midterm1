def deep_copy():
    b = [[1, 2, 3], [3, 2, 1], [4, 5, 6], [6, 5, 4]]
    a = []
    for i in range (0, len(b)):
        c = []
        for j in range(0, len(b[i])):
            c.append(b[i][j])
        a.append(c)
    print(a)


deep_copy()