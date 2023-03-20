def main():
    text = input("Input: ").strip()
    print(shorten(text))

def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    string = ""
    for i in word:
        if i not in vowels:
            string = string + i
    return string


if __name__ == "__main__":
    main()