a=int(input("Ведите число:"))
b=int(input("Введите число:"))
c=int(input("Введите число:"))
if a==b==c:
    print(3)
elif a==b or b==c or c==a:
    print(2)
else:
    print(0)
    