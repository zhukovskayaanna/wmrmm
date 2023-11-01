def str(s):
    s=input("ВВедите строку:")

k=0
str(s)
for i in s:
    if i=="а":
        k+=1
if "а" in s:
    s=s.replace("а","о")
print(s,len(s),k)
