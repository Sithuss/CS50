import inflect
p = inflect.engine()
people = []
while True:
    try:
        t = input().strip()
        people.append(t)
    except EOFError:
        break

alts = p.join((people))
print(f"Adieu, adieu, to {alts}")


