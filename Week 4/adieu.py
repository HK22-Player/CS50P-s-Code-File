import inflect
i = inflect.engine()
names = []

while True:
    try:
        name = input('Name:').title()
        names.append(name)
    except EOFError:
        print("")
        break

adieu = i.join(names)
print(f'Adieu, adieu, to {adieu}')