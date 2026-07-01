list = {

}



while True:
    try:
        item = input().strip().upper()
        if item in list:
            list[item] = list[item] + 1
        else:
            list[item] = 1

    except EOFError:
        for _ in sorted(list):
            print(list[_],_)
        break