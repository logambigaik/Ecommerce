burger_dict={

    "(a) Zinger Burger        ":230,
    "(b) Zinger Cheese Burger ":260,
    "(c) Thames Special Burger":320,
    "(d) Beef Burger          ":250,
    "(e) Tower Burger         ":320,
    "(f) Fish Burger          ":260

}

steak_dict ={
    "(g) Arizona Steak ":650,
    "(h) Mushroom Steak":650,
    "(i) Pepper steak  ":650,
    "(j) Polo Tuscany  ":650

}
category='yes'
#burger_item=[]
#burger_qty=[]
#steak_item=[]
#steak_qty=[]
item_choosen={}

while (category.lower() != 'no'):
    print("Please choose the item from menu List:")
    category=str(input("Burger or Steak or No:"))
    if (category.lower() == 'burger'):
        print("")
        print("Burger List")
        print("===========")
        for i,j in burger_dict.items():
            print(i,j)

        burger_item=(input("Please choose the category from menu list(a-f):"))
        burger_qty=(input("Enter the quantity:"))
        item_choosen[burger_item]=burger_qty


    elif (category.lower()== 'steak'):
        print("")
        print("Steak")
        print("======")
        for i,j in steak_dict.items():
            print(i,j)
        steak_item=(input("Please choose the category from menu list(g-j):"))
        steak_qty=(input("Enter the quantity:"))
        item_choosen[steak_item]=steak_qty


print('The item choosen :')
print(item_choosen)
item =''
price=''
#choosen_item=''
#choosen_price=0
result={}
for i,j in item_choosen.items():


    if i == 'a' :
        item=str((list(burger_dict.keys())[0]))
        price=int((list(burger_dict.values())[0])) * int(j)
    elif i == 'b':
        item = str((list(burger_dict.keys())[1]))
        price= int((list(burger_dict.values())[1])) * int(j)
    elif i == 'c':
        item = str((list(burger_dict.keys())[2]))
        price= int((list(burger_dict.values())[2])) * int(j)
    elif i == 'd':
        item = str((list(burger_dict.keys())[3]))
        price = int((list(burger_dict.values())[3])) * int(j)
    elif i == 'e':
        item = str((list(burger_dict.keys())[4]))
        price= int((list(burger_dict.values())[4])) * int(j)
    elif i == 'f':
        item = str((list(burger_dict.keys())[5]))
        price = int((list(burger_dict.values())[5])) * int(j)
    elif i == 'g':
        item = str((list(steak_dict.keys())[0]))
        price = int((list(steak_dict.values())[0])) * int(j)
    elif i == 'h':
        item = str((list(steak_dict.keys())[1]))
        price = int((list(steak_dict.values())[1])) * int(j)
    elif i == 'i':
        item = str((list(steak_dict.keys())[2]))
        price = int((list(steak_dict.values())[2])) * int(j)
    elif i == 'j':
        item = str((list(steak_dict.keys())[3]))
        price = int((list(steak_dict.values())[3])) * int(j)

    print('Item Selected:', item)
    print('Item Qty:', j)
    print('Item Price:',price)
    result[item]=price


total=0
for i,j in result.items():
    total = total+j

print('Total Price:',total)

