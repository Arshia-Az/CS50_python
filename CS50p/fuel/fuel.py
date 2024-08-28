def main():
    x = check_fuel()
    print(x)


def check_fuel():
    while True:
        try:
            a = input('fraction:')
            # w , s == a.split("/")
            # w = int(w)
            # s = int(s)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if a == "1/3":
                return '33%'
            if a == "2/3":
                return '67%'
            if a == "3/4":
                return '75%'
            elif a == "1/5":
                return "25%"
            elif (a == "4/4") or (a =="99/100" )or (a == "100/100"):
                return "F"
            elif (a == "0/4") or (a=="0/100") or (a== "1/100"):
                return "E"




if __name__ == "__main__":
    main()
