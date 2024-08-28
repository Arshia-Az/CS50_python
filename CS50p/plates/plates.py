def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(words):
    words = words.lower()
    num = 0
    d = '0123456789'
    xs = []
    for word in words:
        num += 1
        if word.isdigit():
            xs.extend(word)
            if xs[0] == "0":
                return False
        if word == '.':
            return False

    if not words[:2].isdigit():
        if num > 6:
            return False
        elif num <= 3:
            return False

        elif words[-1].isalpha():
            if words.isalpha():
                for word in words:
                    if word not in d:
                        return True
        elif words[-1].isdigit():
            if words[-2].isdigit():
                return True
            else:
                return False
        else:
            return True

    else:
        return False


if __name__ == "__main__":
    main()
