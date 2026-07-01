def main():
    time = convert(input("Time :"))
    if 7 <= time <= 8 :
         print("Breakfast Time")
    elif 12 <= time <= 13 :
         print("Lunch Time")
    elif 18 <= time <= 19 :
         print("Dinner Time")

def convert(time):
    hour , minute = map(int, time.replace("a.m.", "").replace("p.m.", "").split(":"))
    if "p.m." in time and hour != 12:
        hour + 12
    if "a.m." in time and hour == 12:
        hour = 0
    return hour + minute / 60

if __name__ == "__main__":
    main()