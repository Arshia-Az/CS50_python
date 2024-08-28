import re
import sys

#get element from user and send to parse
def main():
    print(parse(input("HTML: ")))


def parse(s):
    # check user input for link with re
    matches = re.search(r'"(https?://(?:www\.)?youtube\.com(?:/embed)?/(.+[^"]))"', s)
    # if have line send clean link to user // else return None to show
    if matches :
        return f"https://youtu.be/{matches.group(2)}"
    else:
        return None

if __name__ == "__main__":
    main()
