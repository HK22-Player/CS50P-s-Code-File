from validators import email

def main():
    print(validate(input("What's your email address?").strip()))

def validate(s):
    account = email(s)
    if account == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()