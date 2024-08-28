import sys
import csv
from tabulate import tabulate

menu = []
headers = None
def main():
    check_argv()
    x = 0
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)

            for row in reader:

                x += 1
                if x == 1:
                    headers = row
                else:
                    menu.append(row)

        print(tabulate(menu, headers,tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File dose not exist")

def check_argv():
    if len(sys.argv) > 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 2 :
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
