a = int(input("no. 1:"))
b = int(input("no. 2:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

if a>b:
    print(a ,"is bigger")

elif a == b:
    print("they are equal")

else :
    print(b, "is bigger")

print("square of 1st is:" , a*a)
print("square of 1st is:" , b*b)

if a%2 == 0:
    print(a, "is even")
else : print(a , " is odd")

if b%2 == 0:
    print(a, "is even")
else : print(a , " is odd")