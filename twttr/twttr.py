text = input("Input: ").strip()
str = ""
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for i in text:
    if i not in vowels:
        str = str + i
print("Output: " + str)