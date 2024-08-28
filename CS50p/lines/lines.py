import sys


def main():
    check_argv()
    count_lines = 0
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            for line in lines:
                if check_line(line) == False:
                    count_lines += 1
            print(count_lines)

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_argv():
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_line(line: str):
    if line.isspace():
        return True
    elif line.lstrip().startswith("#"):
        return True
    return False


if __name__ == "__main__":
    main()
