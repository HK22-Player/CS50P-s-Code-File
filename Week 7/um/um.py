import re


def main():
    print(count(input("Text: ")))


def count(s):
    text = re.findall(r"\bum\b",s, re.IGNORECASE)
    return len(text)


if __name__ == "__main__":
    main()