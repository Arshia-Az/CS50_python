def main():
    ask_q = input("say:")
    print(value(ask_q))


def value(greeting):
    val = greeting.strip()
    if val.startswith("hello") or val.startswith("Hello"):
        x =  0
    elif val.startswith("h") or val.startswith("H"):
        x =  20
    else:
        x = 100
    return f"${x}"


if __name__ == "__main__":
    main()
