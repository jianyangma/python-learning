"""
File: warhol.py
---------------
ADD YOUR DESCRIPTION HERE
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage
import random

# Name of file that we will use to create the warhol image
IMAGE_FILE = 'images/simba.jpg'


def create_filtered_image(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol program. It creates an
    image object from the image in the file IMAGE_FILE, and then recolors the image
    object.  The parameters to this function are:
      red_scale: A number to multiply each pixels' red component by
      green_scale: A number to multiply each pixels' green component by
      blue_scale: A number to multiply each pixels' blue component by
    This function should return a newly generated image with the appropriately
    scaled color values of the pixels.
    """
    image = SimpleImage(IMAGE_FILE)
    for pixel in image:
        x = pixel.x
        y = pixel.y
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
        image.set_pixel(x, y, pixel)
    return image

def make_warhol():
    """
    This function generates a Warhol-style picture based on the original image in the
    file IMAGE_FILE.  The Warhol image contains "patches" that are different colored
    versions of the original image.  This function returns the Warhol image.
    """
    org = SimpleImage(IMAGE_FILE)
    width = org.width
    height = org.height
    image = SimpleImage.blank(width*3, height*2)
    for i in range(6):
        rand1 = random.randint(0, 19) / 10.00
        rand2 = random.randint(0, 19) / 10.00
        rand3 = random.randint(0, 19) / 10.00
        filtered = create_filtered_image(rand1, rand2, rand3)
        for pixel in filtered:
            x = pixel.x
            y = pixel.y
            if i <= 2:
                image.set_pixel(x + width*i, y, pixel)
            else:
                temp = i - 3
                image.set_pixel(x+width*temp, y + height, pixel)
    return image


def main():
    """
    This program tests your create_filtered_image and make_warhol functions by calling
    those functions and displaying the resulting images.  Feel free to modify this code
    when you are writing your program.  For example, the call to the create_filtered_image
    function is provided to test that function by itself.  Feel free to delete that portion
    of the code when you have the create_filtered_image working, and then just focus on
    the make_warhol function.
    """

    warhol_image = make_warhol()
    if warhol_image != None:
        warhol_image.show()


if __name__ == '__main__':
    main()
