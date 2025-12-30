a = int(input("enter marks of subject 1: "))
b = int(input("enter marks of subject 2: "))
c = int(input("enter marks of subject 3: "))


def avg(x , y, z): 
    ans = (x+y+z)/3
    print("average is : ", ans)
    if ans >= 75: 
        return "distinction"
    elif 75 > ans >= 40:
        return "pass"
    else: 
        return "fail"


res = avg(a , b , c)
print("result: ", res)
