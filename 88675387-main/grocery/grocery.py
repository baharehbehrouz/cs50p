Num_Grocery_list=0
Grocery_List = []
while True:
    try:
        item=input()
        Grocery_List.append(item.upper())
    except EOFError:
        break
Grocery_List=sorted(Grocery_List)
new_output = {z:Grocery_List.count(z) for z in Grocery_List}
# print(new_output)
for k,v in new_output.items():
    print(v,k)
