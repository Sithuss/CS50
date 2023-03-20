from datetime import datep
import sys
import inflect


class Sub:
    def __init__(self, birth):
        self.birth = birth

    def __str__(self):
        return f"{self.birth}"

    def __sub__(self, other):
        p = inflect.engine()
        total = self.birth - other.birth
        ans = (total.days)
        val = ans * 24 * 60
        word = p.number_to_words(val, andword="")
        return f"{Sub(word)} minutes"


def main():
    bbb = input("Date of brith: ")
    value = get_date(bbb)

    birth = Sub(value)
    now = Sub(date.today())
    total = now - birth
    total = total.capitalize()
    print(total)

def get_date(bbb):
    try:
        birth = bbb

        if not "-" in birth:
            sys.exit("Invalid date")
        birth = birth.split("-")
        for i in range(3):
            if not birth[i].isdigit():
                sys.exit("Invalid date")
            birth[i] = int(birth[i])
        return date(birth[0], birth[1], birth[2])
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()