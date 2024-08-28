def main():
    price = check_in_menu()
    price = str(price).replace("\r\n", "")
    a = float(price)
    return f"{a:.2f}"


def check_in_menu():
    x = float()
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while True:
        try:
            food = str(input("item: ").title())
            if food == "":
                raise EOFError
            elif food in menu:
                x += menu.get(food)
                print(f"${x:.2f}")

        except EOFError:
            return x


if __name__ == "__main__":
    print(main())
