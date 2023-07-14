
d={"Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
dd={}
for key,value in d.items():
    # d.update(key.lower(),value)
    dd.update({key.lower():value})
# print(dd)
total=0
while True:
    try:
        item = input("Item:")
        item=item.lower()
        if item in dd:
            key = dd[item]
            # print(key)
            total+=key

            t="$"+str('%2.2f' % total)
            print("Total:",t)
    except EOFError:
        print("\n")
        break
