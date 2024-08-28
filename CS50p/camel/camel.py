# get word and send to change
def main():
    words = input("camel case: ")
    if not words.islower():
        word = change_name(words)
        return word
    else:
        return words


# edit word
def change_name(words):
    x = list()
    edit_words = words.replace(" ", "")
    for word in edit_words:
        if word.isupper():
            edit_word = word.lower()
            x.extend(f"_{edit_word}")
        else:
            x.extend(word)
    return "".join(x)


if __name__ == "__main__":
    print(main())
