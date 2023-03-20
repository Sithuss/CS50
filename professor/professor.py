import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        integer1 = generate_integer(level)
        integer2 = generate_integer(level)
        ans = integer1 + integer2
        counter = 0

        while True:
            if counter == 3:
                print(f"{integer1} + {integer2} = {ans}")
                break
            try:
                quest = int(input(f"{integer1} + {integer2} = "))
            except ValueError:
                counter = counter + 1
                print("EEE")
                pass
            else:
                if quest == ans:
                    if counter == 0:
                        score = score + 1
                    break

                else:
                    counter = counter + 1
                    print("EEE")

    print("score: ", score)





def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 3 or level < 1:
                pass
            else:
                return level


def generate_integer(level):
    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    else:
        integer = random.randint(100, 999)

    return integer




if __name__ == "__main__":
    main()