import emoji


def main():
    return show_emoji()


def show_emoji():
    say_emoji = input("input: ")
    print(emoji.emojize(say_emoji , language='alias'))


if __name__ == "__main__":
    main()
