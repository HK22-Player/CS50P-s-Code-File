def main() :
    interpreter = input('Expretions :')
    x,y,z = interpreter.split(' ')
    x = float(x)
    z = float(z)
    operator = str_to_operator(y)
    if operator :
        ans = operator(x,z)
        print(ans)
    else :
        None

import operator

def str_to_operator(n):
    if n == '+':
        return operator.add
    elif n == '-':
        return operator.sub
    elif n == '*':
        return operator.mul
    elif n == '/':
        return operator.truediv
    elif n == '^':
        return operator.xor
    elif n == '%':
        return operator.mod
    else :
        None

main()