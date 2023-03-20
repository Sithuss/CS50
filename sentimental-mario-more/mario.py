# TODO
def main():
    height = get_height()
    for i in range(height):
        s = height - i - 1
        j = i + 1
        # print
        print(" " * s, end="")
        print("#" * j, end="")
        print(" " * 2, end="")
        print("#" * j)


def get_height():
    while True:
        try:
            # prompt for height
            n = int(input("Height: "))
            # check
            if n > 0 and n < 9:
                return n
        except ValueError:
            return get_height()


main()