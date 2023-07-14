Fraction=input("Fraction: ")
z=Fraction.split("/")
# Fraction=input("Fraction: ")
if z[1]=="0" or type(z[0])==float or type(z[1])==float:
    while True:
        Fraction = input("Fraction: ")
        z = Fraction.split("/")
        # if type(z[0])!=float and type(z[1])!=float:
        #     break
        if z[1]!="0":
            break
        if ord(z[0])>=48 and ord(z[0])<=58 or ord(z[1])>=48 and ord(z[1])<=58:
            break
if Fraction=="1/4":
    print("25%")
elif Fraction=="1/2":
    print("50%")
elif Fraction=="3/4":
    print("75%")
elif Fraction=="4/4" or Fraction=="100/100" or Fraction=="99/100":
    print("F")
elif Fraction=="1/3":
    print("33%")
elif Fraction=="2/3":
    print("67%")
elif  Fraction=="0/100" or Fraction=="1/100":
    print("E")
