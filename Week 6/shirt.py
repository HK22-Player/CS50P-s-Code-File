import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3 :
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3 :
    sys.exit("Too many command-line arguments")

type = ['.png','.jpg','.jpeg']
input = os.path.splitext(sys.argv[1])[1].lower()
output = os.path.splitext(sys.argv[2])[1].lower()
if input not in type:
    sys.exit("Invalid input")
if output not in type:
    sys.exit("Invalid output")
if input != output:
    sys.exit("Input and output have different extensions")

def main():
    try:
        photo = Image.open(sys.argv[1])
    except:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    fit = ImageOps.fit(photo, size)
    fit.paste(shirt, shirt)
    fit.save(sys.argv[2])

if __name__ == "__main__":
    main()