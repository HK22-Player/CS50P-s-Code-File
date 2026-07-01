i = int(50)
print('Amount Due:',str(i))

while i > 0:
    coin = int(input("Insert Coin:"))
    if coin == 25 or coin == 10 or coin == 5:
        i -= coin
        print('Amount Due:',str(i))
    else :
        print('Amount Due:',str(i))

if i < 0:
    i = -i
    print("Change Owed:", str(i))
else :
    print("Change Owed: 0")