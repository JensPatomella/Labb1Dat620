def loadtxt(filename):
    try:
        file = open(filename)
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        return
    rows = file.readlines()
    file.close()
    M=[]
    for row in rows:
        a = row.split()
        for i in range(len(a)):
            a[i] = float(a[i])
        M.append(a)
    return M
print(loadtxt("chirps.txt"))