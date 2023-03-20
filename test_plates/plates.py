def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for i in s:
        if i.isdigit():
            if i == "0":
                return False
            break

    for j in range(len(s)):
        if s[j].isdigit():
            if j + 1 < len(s):
                if not s[j + 1].isdigit():
                    return False

    if not s[0:2].isalpha():
        return False

    elif not 6 >=  len(s) >= 2:
        return False

    elif not s.isalnum():
        return False

    else:
        return True

if __name__ == "__main__":
    main()