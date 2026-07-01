import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        remainder = 3
        while remainder > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score = score + 1
                    break
                else:
                    print("EEE")
                    remainder = remainder - 1
            except ValueError:
                remainder = remainder - 1
                print('EEE')
                pass
        if remainder == 0:
            print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input('Level:'))
            if n in [1,2,3]:
                return n
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()