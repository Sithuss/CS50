def main():
    time = input("What time is it? ")
    ctime = convert(time)
    if 7 <= ctime <= 8:
        print("breakfast time")
    elif 12 <= ctime <= 13:
        print("lunch time")
    elif 18 <= ctime <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")

    pluser = float(minute) / 60
    result = int(hour) + pluser
    return result

if __name__ == "__main__":
    main()