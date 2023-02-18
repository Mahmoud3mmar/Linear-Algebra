
def CalculateEquation():
    Xi = 0
    print(" Please Enter Your (X node) Value :")
    Xo = int(input());

    print(" Please Enter Your (a) Value :")
    a = int(input());

    print(" Please Enter Your (C) node Value :")
    C = int(input());

    Rn = 0

    print(" Please Enter Your (m) node Value :")
    m = int(input());




    PrimeChecker = isprime(m)
    ZeroChecker = EqualZero(C)
    if(PrimeChecker==True):
        if(ZeroChecker==True):
            Period = m - 1
            print("Period is :",Period)


    if(PrimeChecker==False):
        if (ZeroChecker == True):
            Period = m / 4
            print("Period is :",Period)
        else:
            Period = m
            print("Period is :",Period)

    y = 0
    k = 0
    while True:
        Xi = (Xo * a + C) % m
        Rn = Xi / m
        if k != Xi:
            print("Random Number is :", Rn)
        x = Xi
        k = Xi
        if y == int(Period):
            print("hiii")
        y += 1


def isprime(num):
    if (num> 1):
        for n in range(2,num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False


def EqualZero(num):
    if(num==0):
        return True
    else:
        return False




CalculateEquation()


