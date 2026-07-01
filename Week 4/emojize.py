import emoji

def main():
    data = input('Input:')
    print('Output:',emoji.emojize(data,language='alias'))
main()