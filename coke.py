money=50

while money>0:
    print(f"Amount Due: {money}")
    Coin= int(input("Insert Coin: "))
    if Coin==5:
        money=money-5
    elif Coin==10:
        money=money-10
    elif Coin==25:
        money=money-25
    else:
        money=money-0
    
if money<0:
    print(f"Change Owed: {money*-1}")
else:
    print(f"Change Owed: {money}")
        

    