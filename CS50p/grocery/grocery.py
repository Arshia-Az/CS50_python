gerocery = {}

while True:
    try:
        item = input().lower()
        if item in gerocery:
            gerocery[item] += 1
        else:
            gerocery[item] = 1
    except EOFError:
        for key in sorted(gerocery.keys()):
            print(gerocery[key], key.upper())
        break
