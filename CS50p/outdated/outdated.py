months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def main():
    return outdated()


def outdated():
    year = None
    month = None
    day = None

    while True:
        try:
            # get date form user
            get_date = input("what's date: ")
            # split date and save in x
            times = get_date.split("/")
            if len(times) == 3:
                # check the input don't none
                if get_date != "":
                    # extract the value of times in time
                    for time in times:
                        time = time.strip()
                        # check is time integer
                        if time.isdigit():
                            #  change time to integer and check the count of time
                            if int(len(time)) > 2:
                                #  save the time in to the year
                                year = time
                            else:
                                # check the month is none?
                                if month is None:
                                    # check the count of time
                                    if len(time) == 1:
                                        # save time in month if size of time == 1
                                        month = f"0{time}"
                                    else:
                                        # save time in month
                                        month = time
                                # check the days is none?
                                elif day is None:
                                    # check the count of time
                                    if len(time) == 1:
                                        # save time in day if size of time == 1
                                        day = f"0{time}"
                                    else:
                                        # save time in day
                                        day = time
            else:
                # split get time with "," and save in times
                times = get_date.split(',')
                # get member of times and save in time
                for time in times:
                    # delete white space in time
                    time = time.strip()
                    #check time is not number
                    if not time.isdigit():
                        # save day if have 1 number like this = 0x
                        day = f"0{time[-1]}"
                        # check day is number
                        if day.isdigit():
                            
                            x = time.replace(f" {time[-1]}", '')
                            if x in months:
                                m = str(months[x])
                                if len(m) == 1:
                                    month = f"0{months[x]}"
                                else:
                                    month = m

                    else:
                        year = time

        except TypeError or ValueError:
            pass
        else:
            if month is not None:
                if int(month) <= 12:
                    if day is not None:

                        if int(day) <= 31:
                            print(f"{year}-{month}-{day}", end="")
                            break
                    else:
                        main()
            else:
                main()


if __name__ == "__main__":
    main()
