N = int(input("Введите размерность квадратной матрицы A: "))
A = []
for i in range(N):
    r = []
    for j in range(N):
        element = int(input(f"Введите элемент A[{i}][{j}]: "))
        r.append(element)
    A.append(r)
def matrix(A):
    itog_matrix = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < 0:
                itog_matrix[i][j] = 0
            elif A[i][j] > 0:
                itog_matrix[i][j] = 1

    for i in range(len(itog_matrix)):
        for j in range(len(itog_matrix[i])):
            if j <= i:
                print(itog_matrix[i][j], end=" ")
        print()
matrix(A)

