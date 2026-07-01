while True:
    try:
        x,y = input('Fraction :').split('/')
        x,y = int(x),int(y)
        if y < x:
            raise ValueError
        elif y == int(0):
            raise ZeroDivisionError
        elif  x < int(0):
            raise ValueError
        else:
            break
    except (ValueError, ZeroDivisionError):
        pass

Fullness = x / y * 100
if int(99) <= Fullness <= int(100):
    print("F")
elif int(0) <= Fullness <= int(1):
    print('E')
else:
    print(f'{round(Fullness)}%')