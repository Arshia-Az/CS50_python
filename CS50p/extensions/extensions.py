get_in = input("File name:")


def ext():
    z = get_in.strip().lower()

    if z.endswith(".gif"):
        print(f"image/gif")
    elif z.endswith(".jpg") or get_in.endswith(".jpeg"):
        print("image/jpeg")
    elif z.endswith(".png"):
          print(f"image/png")
    elif z.endswith("pdf") or get_in.endswith("PDF"):
        print("application/pdf")
    elif z.endswith(".txt"):
        x , y = z.split(".", 1)
        print(f"text/{x}")
    elif z.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
ext()

