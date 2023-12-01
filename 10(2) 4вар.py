def max(matrix):
    max_s = float('-inf')
    max_r = []
    for r in matrix:
        if sum(r) > max_s:
            max_s = sum(r)
            max_r = r
    return max_r, max_s


def min(matrix):
    min_s = float('inf')
    min_r = []
    for r in matrix:
        if sum(r) < min_s:
            min_s = sum(r)
            min_r = r
    return min_r, min_s


with open('Zhukovskaya_vvod_Y-233.txt', 'r') as file:
    matrix = [[int(num) for num in line.split()] for line in file]

max_r, max_s = max(matrix)
min_r, min_s = min(matrix)


with open('Zhukovskaya_vivod_Y-233.txt', 'w') as file:
    file.write(f"Строка с наибольшей суммой элементов: {max_r}, сумма: {max_s}\n")
    file.write(f"Строка с наименьшей суммой элементов: {min_r}, сумма: {min_s}\n")
