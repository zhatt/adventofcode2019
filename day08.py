#!/usr/bin/env python3

import aoc


def find_fewest_zero_layer(image, width, height):
    layer_size = width * height
    fewest_0 = layer_size
    result = -1

    # Walk layers and count zeros.
    for index in range(0, len(image), layer_size):
        num_0 = image.count("0", index, index + layer_size)
        if 0 < num_0 < fewest_0:
            fewest_0 = num_0

            # Found a new candidate layer.  Count ones and twos to calculate result.
            num_1 = image.count("1", index, index + layer_size)
            num_2 = image.count("2", index, index + layer_size)
            result = num_1 * num_2

    return result


def render_image(image, width, height):
    layer_size = width * height

    pixels = [' '] * layer_size

    for index, pixel in enumerate(image):
        image_index = index % layer_size
        if pixels[image_index] == ' ':  # is transparent
            if pixel == '0':
                pixels[image_index] = '0'  # black
            elif pixel == '1':
                pixels[image_index] = '1'  # black

    final_image = ''
    for index, pixel in enumerate(pixels):
        if pixel == '1':
            pixel = 'X'
        else:
            pixel = ' '
        final_image += pixel
        if (index + 1) % width == 0:
            final_image += '\n'

    return final_image


IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6


def part1(input_list):
    return find_fewest_zero_layer(input_list[0], IMAGE_WIDTH, IMAGE_HEIGHT)


def part2(input_list):
    image = render_image(input_list[0], IMAGE_WIDTH, IMAGE_HEIGHT)
    # Print the image for debugging.
    # print(image)
    return image


if __name__ == "__main__":
    aoc.main(part1, part2)
