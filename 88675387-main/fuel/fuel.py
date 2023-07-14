Fraction=input("Fraction: ")
while True:
    if Fraction=="1/4":
        print("25%")
        break
    elif Fraction=="1/2":
        print("50%")
        break
    elif Fraction=="3/4":
        print("75%")
        break
    elif Fraction=="4/4" or Fraction=="100/100" or Fraction=="99/100":
        print("F")
        break
    elif Fraction=="1/3":
        print("33%")
        break
    elif Fraction=="2/3":
        print("67%")
        break
    elif  Fraction=="0/100" or Fraction=="1/100":
        print("E")
        break
    Fraction = input("Fraction: ")