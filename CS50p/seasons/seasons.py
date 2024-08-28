from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birthday = input("Date of Birth:")
    try:
        year, month, day = check_time(birthday)
    except:
        sys.exit("Invalid date")
    else:
        formating_birthday =  date(int(year), int(month), int(day))
        curent_day = date.today()
        diff = curent_day - formating_birthday
        total_min = diff.days * 24 * 60

        words = p.number_to_words(total_min, andword="")
        print(f"{words.capitalize()} minutes")

def check_time(s):
    matches = re.search(r"\b\d{4}-\d{2}-\d{2}\b", s)
    if matches:
        year, month, day = s.split("-")
        return year, month, day

if __name__ == "__main__":
    main()
