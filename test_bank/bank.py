def main():
    greet = input("Greeting: ")
    val = value(greet)
    print(f"${val}")


def value(greeting):
    greet = greeting.strip().lower()
    alpha = greet.split()[0]
    if alpha == "hello":
        return 0
    elif alpha[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()