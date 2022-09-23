def lcm(n1,n2):

    if n1<=n2:
        min=n2

    else:
        min = n1

    for i in range (1,min+1):
        if n1%i == 0 and n2%i == 0:
            GCD = i

        LCM = (n1*n2)//GCD

    return LCM

n1 = int(input("Entedr the 1st number: "))
n2 = int(input("Entedr the 2nd number: "))
print("The lcm of two number: ",lcm(n1,n2))