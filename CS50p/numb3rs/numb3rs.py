import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if check_ip := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        if int(check_ip.group(1)) <= 255 and int(check_ip.group(2)) <= 255 and int(check_ip.group(3)) <= 255 and int(check_ip.group(4)) <= 255:
            return True
        else:
            return False
    return False


if __name__ == "__main__":
    main()

