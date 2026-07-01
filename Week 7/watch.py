import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.search(r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)".*?></iframe>',s)
    if link:
        code = link.group(1)
        return f"https://youtu.be/{code}"
    return None

if __name__ == "__main__":
    main()