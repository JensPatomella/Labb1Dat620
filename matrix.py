def transpose(matrix): #Antar man kan kolla på elementet i column n och sen lägga den i en rad n
    column = 0
    matrix_transpose = []
    row_transpose = []
    rows_in_matrix = len(matrix)

    for entry in range(len(matrix[0])): #Antalet columner
        column = entry
        
        for row_entry in range(rows_in_matrix): #Antalet rader att gå igenom 
            element_transpose = (matrix[row_entry])[column] #Vilket element i column n rad m den ska kolla på
            row_transpose.append(element_transpose) #row = row + [new entry], Lägger till det nya elementet i en rad

            if len(row_transpose) == int(len(matrix)):
                matrix_transpose.append(row_transpose)
                row_transpose = []

    return matrix_transpose

def powers(list,start_power,end_power): #Antar att start_ end_ kommer vara det vi ska iterera över
    row = []
    new_matrix = []
    entries_in_list = len(list)
    for entry_n in range(entries_in_list): #Antalet element att gå igenom
        element = list[entry_n] #Vilket element i listan den ska kolla på
        for power in range(start_power,end_power): #Elementet ska upphöjas, läggas i en lista, sen tar listan slut när alla element har använts
            new_entry = element**power
            row.append(new_entry) #row = row + [new entry], Lägger till det nya elementet i en rad
            if len(row) == end_power:
                new_matrix.append(row)
                row = []
    return new_matrix

def matmul(M, N):
    return

def invert(M):
    return

def loadtxt(filename):
    try:
        file = open(filename) #försöker öppna filen med namn {filename} går det ej returnerar den none
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        return
    rows = file.readlines() #sparar en lista av textfilens rader
    file.close() #stänger textfilen
    M=[]
    for row in rows:
        a = row.split() #delar upp rader vid blanksteg
        for i in range(len(a)):
            try:
                a[i] = float(a[i])
            except ValueError:
                print(f"Error: '{filename}' contains invalid values")
                return
        M.append(a)
    return M
print(loadtxt("chirps.txt"))