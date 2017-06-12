from PIL import Image
import turtle

img = Image.open("finch.jpg")
width, _ = img.size
for i, px in enumerate(img.getdata()):
    if sum(px[:3]) > 128 * 3:
        newColor = (255, 255, 255, 255)
    else:
        newColor = (0, 0, 0, 255)
    y = i // width
    x = i % width
    img.putpixel((x, y), newColor)

# img.show()

def turtleSpiral(speed=3, spacing = 5):
    print(turtle.pos())
    radius = 1
    while True:
        turtle.forward(speed)
        turtle.left(speed * 360 / 2 / 3.14159 / radius)
        radius += spacing * speed / 2 / 3.14159 / radius

def turtleImgSpiral(img, speed=0.5, spacing = 2):
    radius = 1

    width, height = img.size
    x0, y0 = (width//2, height//2)


    while True:
        # Read the turtle's position and get it in the image
        pos = turtle.position()
        x, y = (int(pos[0]), -int(pos[1]))
        try:
            r, g, b = img.getpixel((x + x0, y + y0))
            if r > 0:
                turtle.penup()
            else:
                turtle.pendown()
        except IndexError:
            turtle.penup()

        # Move turtle in spiral
        spd = speed * radius**0.5
        turtle.forward(spd)
        turtle.left(spd * 360 / 2 / 3.14159 / radius)
        radius += spacing * spd / 2 / 3.14159 / radius

turtleImgSpiral(img)

input()
