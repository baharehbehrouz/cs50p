
lstNames=[]
while True:
    try:
            Name=input('Name: ')
            lstNames.append(Name)

    except EOFError:
        print("\n")
        break
out="Adieu, adieu, to "

for item in lstNames:
    if len(lstNames)==1:
        out+=item
    elif len(lstNames)==2:
        if lstNames.index(item)==0:
            out += item + " and "
        elif  lstNames.index(item)==1:
            out += item
    elif len(lstNames)>2:
        if lstNames.index(item)==len(lstNames)-2:
            out+=item+", and "
        elif lstNames.index(item)!=len(lstNames)-1:
            out += item + ", "
        else:
            out+=item


print(out)