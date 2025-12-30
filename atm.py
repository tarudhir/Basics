bal = 500000
choice = input("what do you want to do? deposit, withdraw check")



def banking(x , y, z):
    if y.lower() == "deposit":
        a = x + z
        return "new balance is " , a
    
    
    elif y.lower() == "withdraw":
        if x >= z:
            c = x-z
            return "withdraw successful. New balance = " , c

        elif x < z:
            return "insufficient balance"
        

if choice.lower() == "check":
    print("balance is:" , bal )

else: 
    amt = int(input("what amount "))
    out = banking(bal , choice, amt) 
    print (out)




