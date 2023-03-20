# TODO
def main():
    height = get_height()
    for i in range(height):
        s = height - i - 1
        j = i + 1
        # put space
        print(" " * s, end="")
        # put hash
        print("#" * j)


def get_height():
    while True:
        try:
            n = int(input("Height:"))
            # check value range
            if n > 0 and n < 9:
                return n
                # ask again loop
        except ValueError:
            return get_height()


main()
