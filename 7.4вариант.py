def f(n):
    A=[]
    for i in range(1,n+1):
        A.append(int(input("Введите число:")))
    max=0
    k=0
    for t in range(len(A)):
        if A[t]>max:
            max=A[t]
            k=t
    print(max,k)

n=int(input("Введите количество чисел:"))
f(n)




