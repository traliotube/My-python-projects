from PIL import Image, ImageDraw, ImageFont
import string
import random
import sys


def random_string():
    N = 5
    s = string.ascii_uppercase + string.ascii_lowercase + string.digits
    random_string = ''.join(random.choices(s, k=N))
    return random_string


def get_random_x_y(): return (random.randrange(5, 85), random.randrange(5, 55))


colors = ["black", "red", "blue", "green",
          (64, 107, 76), (0, 87, 128), (0, 3, 82)]

fill_color = [(64, 107, 76), (0, 87, 128), (0, 3, 82),
              (191, 0, 255), (72, 189, 0), (189, 107, 0), (189, 41, 0)]


def gen_captcha_img():
    img = Image.new('RGB', (90, 60), color="white")
    draw = ImageDraw.Draw(img)

    captcha_str = random_string()
    text_colors = random.choice(colors)
    font_name = "src\FiraCode-Regular.ttf"
    font = ImageFont.truetype(font_name, 18)
    draw.text((20, 20), captcha_str, fill=text_colors, font=font)

    for i in range(5, random.randrange(10, 15)):
        draw.line((get_random_x_y(), get_random_x_y()), fill=random.choice(
            fill_color), width=random.randrange(1, 3))

    for i in range(10, random.randrange(31, 36)):
        draw.point((get_random_x_y(), get_random_x_y(), get_random_x_y(), get_random_x_y(), get_random_x_y(), get_random_x_y(
        ), get_random_x_y(), get_random_x_y(), get_random_x_y(), get_random_x_y()), fill=random.choice(colors))

    img.save("captcha_img/" + captcha_str + ".png")

    return True


x = 0

try:
    no_of_captchas = input("Enter Number of Captchas to generate:")
except ValueError:
    print("Please enter a number")
    sys.exit()

while x < int(no_of_captchas):
    gen_captcha_img()
    x += 1
