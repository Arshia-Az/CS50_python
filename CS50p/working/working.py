import re


def main():
    print(convert(input("Hours: ")))



def convert(s):
    #check the time and spilt time
    if matches := re.search(r"^([0-9]+):?([0-9]+)? (AM|PM) to ([0-9]+):?([0-9]+)? (AM|PM)$", s ):
        # get the min from matches
        min_1 = matches.group(2)
        min_2 = matches.group(5)
        # check the min is not none if is none change the value to 00
        if min_1 is None:
            min_1 = "00"
        if min_2 is None:
            min_2 = "00"

        # get the hour from matches
        hour_1 = matches.group(1)
        hour_2 = matches.group(4)

        # get the AM or PM from matches
        am_or_pm = matches.group(3)
        am_or_pm2 = matches.group(6)

        # check the hour is 12 or not
        if hour_1 == "12" or hour_2 == "12":
            if am_or_pm == "AM":
                hour_1 = "00"
                if am_or_pm2 == "PM":
                    hour_2 = "12"
                    return f"{hour_1}:{min_1} to {hour_2}:{min_2}"

            # todo: check the better

        else:
            if int(hour_1) <= 12 and int(hour_2) <= 12:
                if int(min_1) < 60 and int(min_2) < 60:
                    #check the is first time is am or pm
                    if am_or_pm == "AM":
                        if am_or_pm2 == "AM":
                            return f"0{hour_1}:{min_1} to 0{hour_2}:{min_2}"
                        else:
                            hour_2 = int(hour_2)
                            hour_2 += 12
                            return f"0{hour_1}:{min_1} to {hour_2}:{min_2}"
                    else:
                        hour_1 = int(hour_1)
                        hour_1 += 12
                        if am_or_pm2 == "AM":
                            return f"{hour_1}:{min_1} to 0{hour_2}:{min_2}"
                        else:
                            hour_2 = int(hour_2)
                            hour_2 += 12
                            return f"{hour_1}:{min_1} to {hour_2}:{min_2}"
                else:
                    raise ValueError
            else:
                raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()



