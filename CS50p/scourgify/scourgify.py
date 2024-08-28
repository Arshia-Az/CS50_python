import sys
import csv


def main():
    print(sys.argv[1],sys.argv[2])
    check_argv()

    out_put = []

    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["name"].split(",")

                out_put.append({"first":name[1].lstrip(), "last":name[0], "house":row["house"]})


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}!")


    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first":"first", "last":"last", "house":"house"})

        for row in out_put:
            writer.writerow({"first": row["first"],"last":row["last"], "house":row["house"] } )


#get to arg from user
def check_argv():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("File is not csv")


if __name__ == "__main__":
    main()
