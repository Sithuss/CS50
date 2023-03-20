def main():
    print("Amount Due: 50")
    coin = get_cents()
    cost = 50
    res = cost - coin
    while res > 0:
        print(f"Amount due: {res}")
        coin = get_cents()
        res = res - coin
    if res <= 0:
        res = format(res).replace("-", "")
        print(f"Change owed: {res}")

def get_cents():
    while True:
        cents = int(input("Insert coin: "))
        if cents == 25 or cents == 10 or cents == 5:
            return cents
        else:
            return main()


main()