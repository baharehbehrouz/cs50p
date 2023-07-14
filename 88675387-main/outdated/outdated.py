
Month=[
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

while True:
        Date=input("Date: ")
        Date=Date.strip()
        if "/" in Date:
            arr=Date.split('/')
        elif " " in Date:
            arr=Date.split(" ")
        # i=0
        if not arr[0].isdigit() and not arr[1].isdigit() and ',' in arr[1]:
            for i in Month:
                 if arr[0].lower()==i.lower():
                        ind=Month.index(i)
                        # print("found")
                        arr[0]=str(ind+1)
                        # arr[0] = str(Month.index(arr[0].lower()) + 1)
                        arrInMonth=True
            # if not arr[1].isdigit() and ',' in arr[1]:
                        arr[1]=arr[1].replace(',','')
                        Date = arr[1] + '/' + arr[1] + '/' + arr[2]
        # print(arr)

        if len(arr) == 3 and len(Date) <= 10 and len(Date) >= 8 and len(arr[2]) == 4 and int(arr[0])>=1 and int(arr[0])<=12 and int(arr[1])>=1 and int(arr[1])<=31:
            break
# print(arr)
if len(arr[0])==1 or len(arr[1])==1:
    arr[0] = int(arr[0])
    arr[0] = f"{arr[0]:02}"
    arr[1] = int(arr[1])
    arr[1] = f"{arr[1]:02}"
Date=arr[2]+'-'+arr[0]+'-'+arr[1]
print(Date)