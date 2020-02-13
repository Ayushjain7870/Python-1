lists=[]
ID=[]
costs=[]
q=10
i=0
while q==10:
    print("What do you want to do?\n 1: Add item\n2: Create bill list\n3:Cost\n 4:Print\n")
    x=int(input("Your option "))
    while x==1:
        name=str(input("Enter Item name "))
        identity=str(input("Enter Item ID "))
        cost=int(input("Enter cost"))
        lists.append(name)
        ID.append(identity)
        costs.append(cost)
        print("To end adding items and calculate bill press 2,or to add more items press 1")
        x=int(input("Your option:"))
    while x==2 and lists=='':
        print("create a list first")
    while x==2 and lists!='':
        print("You have chosen to create bill list")
        y=int(input("Enter product id"))
        while i<=len(ID):
            if y==ID[i]:
                price=costs[i]
            else:
                print("Select valid ID")
            i=i+1
        print("To display bill press 3,or to add more items press 2")
        x=int(input("Your Option"))
    while x==3:
        print("Your total amount is",price)
        q=0
        x=4
    while x==4:
        break
        










            
