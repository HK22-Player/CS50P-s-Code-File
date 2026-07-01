import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font = figlet.getFonts()

if len(sys.argv) == 1:
    random_font = random.choice(font)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    random_font= sys.argv[2]
    if random_font not in font:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

data = input("Input: ")

figlet.setFont(font = random_font)
print(figlet.renderText(data))