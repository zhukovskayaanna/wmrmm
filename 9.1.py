a = int(input("Введите количество строк: "))
c = int(input("Введите количество столбцов: "))
matrix = []
for i in range(a):
    r = list(map(int, input(f"Введите элементы строки {i + 1}, разделенные пробелом: ").split()))
    matrix.append(r)
def ms (matrix):
    max_ = sum(matrix[0])
    min_ = sum(matrix[0])
    max_z = matrix[0]
    min_z = matrix[0]

    for z in matrix[1:]:
        zsum = sum(z)

        if zsum > max_:
            max_ = zsum
            max_z = z

        if zsum < min_:
            min_ = z
            min_z = z

    return max_z, max_, min_z, min_

max_z, max_, min_z, min_ = ms (matrix)

print("Строка с наибольшей суммой элементов:", max_z)
print("Строка с наименьшей суммой элементов:", min_z)
print("Сумма элементов наибольшей строки:", max_)
print("Сумма элементов наименьшей строки:", min_)

