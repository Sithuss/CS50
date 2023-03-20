val = {}
while True:
    try:
        item = input().upper().strip()
        if item not in val.keys():
            val[item] = 1
        else:
            val[item] = val[item] + 1

    except EOFError:
        print("")
        break
sort_i = sorted(val.keys())
for i in sort_i:
    print(val[i], i)