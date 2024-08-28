import sys
from PIL import Image, ImageOps

def main():
    check_argv()

    try:
        get_image = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")
    else:
        shirt = Image.open("shirt.png")
        size = shirt.size
        make_picture = ImageOps.fit(get_image, size)
        make_picture.paste(shirt, shirt)
        make_picture.save(sys.argv[2])
def check_argv():
    valid_extention = [".jpg", ".png", ".jpeg"]
    e1 = sys.argv[1].split('.')
    e2 = sys.argv[2].split('.')
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not any(sys.argv[1].endswith(ext) for ext in valid_extention):
        sys.exit("Invalid output")
    elif not any(sys.argv[2].endswith(ext) for ext in valid_extention):
        sys.exit("Invalid output")
    elif not e1[1] == e2[1]:
        sys.exit("Input and output have different extensions")


def merge(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

if __name__ == "__main__":
    main()
