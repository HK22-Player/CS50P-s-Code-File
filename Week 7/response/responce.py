from validators import email

def main():
    account = input("What's your email address?").strip()
    if email(account) == True:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()