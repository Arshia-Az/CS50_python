def main():
    times = input("what time is it?")
    time = convert(times)
    time.strip()
    hour, min =time.split(".")
    if (hour == "7") or (hour == "8"):
        print("breakfast time")
    elif (hour == "12") or (hour == "13"):
        print("lunch time")
    if (hour == "18") or (hour == "19"):
        print("dinner time")




def convert(time):
    hour, min =time.split(":")
    if min == "30":
        return f"{hour}.5"
    elif min == "15":
        return f"{hour}.25"
    elif min == "00":
        return f"{hour}.0"
    else:
        return f"{hour}.{min}"



if __name__ == "__main__":
    main()
