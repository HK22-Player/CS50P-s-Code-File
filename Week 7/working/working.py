import re


def main():
    print(convert(input("Hours: ")))


def convert(s):

    time = re.search(r"^(\d+)(?::(\d{2}))? (AM|PM) to (\d+)(?::(\d{2}))? (AM|PM)$",s)
    if time :
        hours = list(time.groups())

        if hours[1] is None:
            hours[1] = "00"

        if hours[4] is None:
            hours[4] = "00"

        if int(hours[0]) < 1 or int(hours[0]) > 12:
            raise ValueError
        if int(hours[3]) < 1 or int(hours[3]) > 12:
            raise ValueError

        if int(hours[1]) < 0 or int(hours[1]) > 59:
            raise ValueError
        if int(hours[4]) < 0 or int(hours[4]) > 59:
            raise ValueError

        if hours[2] == "AM" and hours[0] == "12":
            hours[0] = "00"
        if hours[5] == "AM" and hours[3] == "12":
            hours[3] = "00"

        if hours[2] == "PM" and hours[0] != "12":
            hours[0] = str(int(hours[0]) + 12)
        if hours[5] == "PM" and hours[3] != "12":
            hours[3] = str(int(hours[3]) + 12)

        alltime = [hours[0],hours[1],hours[3],hours[4]]

        response = f"{int(alltime[0]):02}:{int(alltime[1]):02} to {int(alltime[2]):02}:{int(alltime[3]):02}"
        return response

    else:
        raise ValueError

if __name__ == "__main__":
    main()