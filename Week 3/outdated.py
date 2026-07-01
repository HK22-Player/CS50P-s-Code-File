months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



while True:
    date = input('Date: ')
    try:
        month,day,year = date.strip().split('/')
        if int(1)<=int(month)<=int(12) and int(1)<=int(day)<=int(31):
            break
    except:
        try:
            old_month,old_day,year = date.split(' ')
            for z in range(len(months)):
                if old_month == months[z]:
                    month = z + 1
                if "," in date:
                    day = old_day.replace(',','')
            if int(1)<=int(month)<=int(12) and int(1)<=int(day)<=int(31):
                break
        except:
            print()
            pass
print(f'{year}-{int(month):02}-{int(day):02}')