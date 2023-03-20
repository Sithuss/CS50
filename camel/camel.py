text = input("camelCase: ").strip()
out = []

for i in text:
    if i.islower():
        out.append(i)
    else:
        out.append("_")
        out.append(i.lower())

print("snake_case: ", end="")
for j in out:
    print(j, end="")
print("")