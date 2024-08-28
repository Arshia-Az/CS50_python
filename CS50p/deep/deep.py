get_q = input("what is answer to the greatquestion of life, the universe, and everyting?")


def check_q():
    val = get_q.strip().lower()
    if val == "42":
        print('Yes')
    elif val == "forty-two":
        print('Yes')
    elif val == "forty two":
        print('Yes')
    else:
        print("No")


if __name__ == "__main__":
    print(check_q())
