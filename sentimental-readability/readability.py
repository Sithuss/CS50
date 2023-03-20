# TODO
from cs50 import get_string


def main():
    # get text
    text = get_string("Text: ")

    letter = letters(text)
    word = words(text)
    sentence = sentences(text)

    # calculate index
    index = (0.0588 * letter / word * 100) - (0.296 * sentence / word * 100) - 15.8
    inde = round(index)

    if inde < 1:
        print("Before Grade 1")

    elif inde > 16:
        print("Grade 16+")

    else:
        print(f"Grade {inde}")

# calculate letters


def letters(text):
    l = 0
    for w in text:
        if w.isalpha():
            l += 1
    return l

# calculate words


def words(text):
    w = text.split()
    count_words = len(w)
    return count_words

# calculate sentences


def sentences(text):
    count = 0
    for l in text:
        if l == "." or l == "?" or l == "!":
            count += 1
    return count


main()