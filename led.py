import pprint
import struct
import binascii

import requests
from xtermcolor import colorize


LED_RANGE = range(0, 60)
COLOUR_RANGE = range(0, 256)


def print_colorized(text, rgb):
    colour = int(binascii.hexlify(struct.pack('BBB', *rgb)).decode('utf-8'), 16)
    print(colorize(text, colour))


def update_led(led_index, colour, dry_run=False):
    colour = colour.strip("#")
    red, green, blue = rgb = struct.unpack('BBB', colour.decode('hex'))
    data = {
        'led-index': led_index,
        'red': red,
        'green': green,
        'blue': blue,
    }

    if dry_run:
        pprint.pprint(data)
        print_colorized("Sample", rgb)
        return

    resp = requests.post(
        'http://gears.djangounderthehood.com/set-led-colour/',
        data=data)
    print_colorized(resp, rgb)
