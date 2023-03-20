def main():
    fuel = get_fuel("Fraction: ")
    if fuel == 1:
        print("F")

    elif 0.99 <= fuel <=1:
        print("F")

    elif 0 <= fuel <= 0.01:
        print("E")

    else:
        print(f"{round(fuel*100)}%")


def get_fuel(prompt):
    try:
        x, y = input(prompt).split("/")
        x = int(x)
        y = int(y)
        if x > y:
            return main()
        res = x / y

    except ValueError:
        return main()
    except ZeroDivisionError:
        return main()
    else:
        return res


main()