greet = input("Greeting: ").strip().lower()
first = greet.split()[0]

if first.replace(",", "") == "hello":
    print("$0")
elif first[0] == "h":
    print("$20")
else:
    print("$100")