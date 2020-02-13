itemlist={1:"Mango",2:"Tango"}
def CreateDatabase():
    n=input("ENTER ITEM")
    p=input("ENTER COST")
    itemlist.update({n:p})
def Costkey():
    for key in itemlist:
        r=itemlist.get(key)
        return r
def ItemValue():
    for Value in itemlist:
        item= itemlist[Value]
        return item  
def PrintTotalList():
    print("  Item  \tCost\n--------------------\n",itemlist)

print("What do you want to do?")
print("Some functions are..")
i=input("1:createlist\n2:createbill")
CreateDatabase()
p=0
q=0
r=0
while p==q:
    r=input("Enter key to find")
    for key in itemlist:
        show=itemlist.get(key)
        if show==r:
            print(show)
        n=input("Do you want to search another item?")
        if n=="no":
            p=9
            break
        else:
            print("Does not exist")
            
print(r,"r")
print(ItemValue())


