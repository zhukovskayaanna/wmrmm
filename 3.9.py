n=int(input("Ведите число:"))
m=int(input("Введите число:"))
k=int(input("Введите число:"))
if k<m*n and(k%n==0 or k%m==0):
    print("Да")
else:
    print("Нет")

