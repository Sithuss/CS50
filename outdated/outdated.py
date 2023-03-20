month = [
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

format = {"January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
def main():
    date = get_date()
    dd = date[1]
    mm = date[0]
    yy = date[2]

    print(f"{yy}-{mm:02d}-{dd:02d}")

def get_date():
    while True:
        data = input("Date: ").strip().title()

        if "/" in data:
            data = data.split("/")
            if data[0].isalpha():
                return get_date()
            data[0] = int(data[0])
            if data[0] > 12:
                return get_date()
        else:
            if "," not in data:
                return get_date()
            data = data.replace(",", "")

            data = data.split(" ")
            if data[0] not in month:
                return get_date()
            else:
                data[0] = format[data[0]]

        try:
            data[2] = int(data[2])
            data[1] = int(data[1])
            if data[1] > 31:
                return get_date()
            return data

        except ValueError:
            pass



main()