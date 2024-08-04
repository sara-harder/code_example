# see full working code here: https://github.com/sara-harder/color-scheme-generator/blob/main/python/main_color.py
from helper import *
def calculate_color(counts, all_pixels, factors):
    """Takes a list of pixel counts, a dictionary of pixels, and boundaries; finds the pixel with the highest count,
    then moves all pixels close to that color from the dict to a new category dict; returns the category dict"""
    highest, cat = max(counts), dict()

    # finds most used color and removes it from dict and count, adding it to category
    color = find_highest(highest, all_pixels)
    rm_pixel(color, highest, all_pixels, counts, cat)

    keys, total = list(all_pixels), highest
    h, s, v = color

    # determines if color is on the greyscale
    bgw = greyscale(s, v, factors[2])
    # establishes range for colors similar to chosen color
    rng = boundaries(h, s, v, factors[0], factors[1])

    # iterates over all pixels not previously eliminated to compare with chosen color
    for pixel in keys:
        count = all_pixels[pixel]
        # performs comparison with chosen color
        if close_color(pixel, bgw, rng, factors[0], factors[2]):
            rm_pixel(pixel, count, all_pixels, counts, cat)
            total += count

    cat["color"] = color
    cat["count"] = total
    return cat