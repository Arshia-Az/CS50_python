def play_back():
    get_word = input("give me the text:")
    return get_word


def main():
    change_speed = play_back().replace(' ', "...")
    return change_speed


print(main())
