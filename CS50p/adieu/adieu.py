import inflect

x = inflect.engine()
names = list()


def say_adieu():
    while True:
        try:
            get_name = input("Name: ")
            names.append(get_name)
        except EOFError:
            print()
            break

say_adieu()

output = x.join(names)

print("Adieu, adieu, to " + output)
