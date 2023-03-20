import random
import sys

def main():
    num = get_int()
    ans = random.randint(1, num)

    while True:
        try:
            guess = int(input("guess: "))
        except ValueError:
            pass
        else:
            if guess < 0:
                pass
            elif guess > ans:
                print("Too large!")
                pass
            elif guess < ans:
                print("Too small!")
                pass
            else:
                print("Just right!")
                sys.exit()

def get_int():
    while True:
        try:
            val = int(input("Level: "))
            if val > 100 or val < 1:
                return get_int()
            else:
                return val
        except ValueError:
            pass



main()
