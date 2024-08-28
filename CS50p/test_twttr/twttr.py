def main():
    messages = input("Input: ")
    output = shorten(messages)
    print(f"output: {output}")


def shorten(word):
    abbreviated_word = ""
    # vowels = "aeiouAEIOU"
    vowels = "aeiouAEIOU"
    for char in word:
        if char not in vowels:
            abbreviated_word += char

    return abbreviated_word


if __name__ == "__main__":
    main()

