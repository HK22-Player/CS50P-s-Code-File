from datetime import date
import inflect
import sys
import re

def main():
    try:
        print(get_birth(input("Date of Birth: ")))
    except (ValueError,TypeError):
        sys.exit("Invalid date")

def get_birth(s):
     matches = re.search(r"^(\d{4})-(\d{2})-(\d{2})$",s)
     if not matches:
         raise ValueError
     birth_time = date.fromisoformat(s)
     p = inflect.engine()
     today = date.today()
     minus = (today - birth_time).days
     if minus < 0:
         raise ValueError
     time = minus*24*60
     word = p.number_to_words(time, wantlist=False).replace(" and ", " ").capitalize()
     return f"{word} minutes"

if __name__ == "__main__":
    main()