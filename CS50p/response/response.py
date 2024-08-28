from validator_collection import validators, checkers

def main():
    print(check_email(input("What's your email address? ")))



def check_email(e):
    checking = checkers.is_email(e)
    if checking:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
