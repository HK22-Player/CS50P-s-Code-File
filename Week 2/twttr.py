vowels = ['a','e','u','i','o','A','E','U','I','O']
words = input('Input: ')
print('Outpur:',end='')

for Letter in words:
    if Letter in vowels:
        pass
    else :
        print(Letter,end='')

print('')