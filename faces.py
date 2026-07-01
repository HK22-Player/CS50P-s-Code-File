def convert(Text):
    Text=Text.replace(":)","🙂")
    Text=Text.replace(":(","🙁")
    print(Text)
def main():
    Text=input()
    convert(Text)

main()