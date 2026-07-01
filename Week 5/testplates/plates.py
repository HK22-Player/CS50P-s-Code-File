def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    elif not s.isalnum():
        return False
    elif not (s[0].isalpha() and s[1].isalpha()):
        return False

    first = len(s) - 1
    found_number = False
    for letter in s:
        if letter.isdigit():
            if letter == '0':
                return False
            first = s.index(letter)
            found_number = True
            break
    if found_number:
        for letter in s[first:]:
            if letter.isalpha():
                return False
    return True

if __name__ == "__main__":
    main()