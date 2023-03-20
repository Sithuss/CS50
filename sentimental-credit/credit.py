# TODO
def main():
    number = get_number()

    # extract all digits from cards
    d1 = int(number % 10)
    d2 = int((number / 10) % 10)
    d3 = int((number % 1000) / 100)
    d4 = int((number % 10000) / 1000)
    d5 = int((number % 100000) / 10000)
    d6 = int((number % 1000000) / 100000)
    d7 = int((number % 10000000) / 1000000)
    d8 = int((number % 100000000) / 10000000)
    d9 = int((number % 1000000000) / 100000000)
    d10 = int((number % 10000000000) / 1000000000)
    d11 = int((number % 100000000000) / 10000000000)
    d12 = int((number % 1000000000000) / 100000000000)
    d13 = int((number % 10000000000000) / 1000000000000)
    d14 = int((number % 100000000000000) / 10000000000000)
    d15 = int((number % 1000000000000000) / 100000000000000)
    d16 = int((number % 10000000000000000) / 1000000000000000)

    # solving Luhan's algorithm
    m2 = d2 * 2
    s2 = int((m2 % 10) + ((m2 / 10) % 10))

    m4 = d4 * 2
    s4 = int((m4 % 10) + ((m4 / 10) % 10))

    m6 = d6 * 2
    s6 = int((m6 % 10) + ((m6 / 10) % 10))

    m8 = d8 * 2
    s8 = int((m8 % 10) + ((m8 / 10) % 10))

    m10 = d10 * 2
    s10 = int((m10 % 10) + ((m10 / 10) % 10))

    m12 = d12 * 2
    s12 = int((m12 % 10) + ((m12 / 10) % 10))

    m14 = d14 * 2
    s14 = int((m14 % 10) + ((m14 / 10) % 10))

    m16 = d16 * 2
    s16 = int((m16 % 10) + ((m16 / 10) % 10))

    sum1 = s2 + s4 + s6 + s10 + s12 + s14 + s16 + s8
    chksum = sum1 + d1 + d3 + d5 + d7 + d9 + d11 + d13 + d15

    if chksum % 10 == 0:
        # print if amex
        if (d15 == 3 and d14 == 7) or (d15 == 3 and d14 == 4):
            print("AMEX")

        # print if mastercard
        elif (d16 == 5 and d15 == 1) or (d16 == 5 and d15 == 2) or (d16 == 5 and d15 == 3) or (d16 == 5 and d15 == 4) or (d16 == 5 and d15 == 5):
            print("MASTERCARD")

        # print if visa
        elif d16 == 4 or d15 == 4 or d14 == 4 or d13 == 4:
            print("VISA")

        # for invalid card type
        else:
            print("INVALID")

    # chksum does not meet conditions
    elif not chksum % 10 == 0:
        print("INVALID")


def get_number():
    while True:
        # check conditions
        try:
            number = int(input("Number: "))
            if number > 0:
                return number
        except:
            return get_number()


main()
