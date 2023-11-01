def f(n):
    A=[]
    for i in range(1,n+1):
        A.append(int(input("Введите число:")))
    a=[]
    for n in A:
        if n%2!=0:
            a.append(n)
    if len(a)==0:
        print("Нечетных нет")
    else:
        a.sort()
        a.reverse()
        print(a)

n=int(input("Введите количество чисел:"))
f(n)




