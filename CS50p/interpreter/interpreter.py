number = input("Expression:")


def calc(num):
    if num.find("+") != -1:
        if num.split("+"):
            x, y = num.split("+")
            z = float(x) + float(y)
        return z
    elif num.find("-") != -1:
        if num.split("-"):
            x, y = num.split("-")
            z = float(x) - float(y)
        return z
    elif num.find("/") != -1:
        if num.split("/"):
            x, y = num.split("/")
            z = float(x) / float(y)
        return z
    elif num.find("*") != -1:
        if num.split("*"):
            x, y = num.split("*")
            z = float(x) * float(y)
        return z


print(calc(number.replace(" ","")))
