def A(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    return matrix

def l(matrix):
    result = []
    for i in range(len(matrix)):
        result.append(matrix[i][:i+1])
    return result

with open('zhukovskaya_Y-233_vvod.txt', 'r') as file:
    matrix = [[int(num) for num in line.split()] for line in file]

new_matrix = A(matrix)

tr= l(new_matrix)

with open('Zhukovskaya_Y-233_vivod.txt', 'w') as file:
    for row in tr:
        file.write(' '.join(map(str, row)) + '\n')



