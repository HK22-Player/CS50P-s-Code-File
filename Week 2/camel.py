#Aplikasi utama
def main():
    name = input('camelCase:')
    print("snakecase ",end=":")
    convert(name)
    print(" ")
#Pengubah
def convert(name):
    for character in name:
        if character.isupper():
            print("_" + character.lower(),end='')
        else:
            print(character,end='')

main()