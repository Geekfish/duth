from __future__ import absolute_import
from time import sleep
from itertools import cycle
import pprint
import struct
import binascii

import requests
from xtermcolor import colorize

from morse import encode


LED_RANGE = range(0, 60)
COLOUR_RANGE = range(0, 256)

RAINBOW = [
    "ff00ff",
    "ff0080",
    "ff0000",
    "ff8000",
    "ffff00",
    "80ff00",
    "00ff00",
    "00ff80",
    "00ffff",
    "007fff",
    "0000ff",
    "7f00ff",
]
RAINBOW_ITER = zip(list(LED_RANGE), cycle(RAINBOW))


def print_colorized(text, rgb):
    colour = int(binascii.hexlify(struct.pack('BBB', *rgb)).decode('utf-8'), 16)
    print(colorize(text, colour))


def update_led(led_index, colour, dry_run=False, retry=2):
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

    for attempt in range(retry):
        resp = requests.post(
            'http://gears.djangounderthehood.com/set-led-colour/',
            data=data)
        print_colorized(resp, rgb)
        if resp.status_code == 200:
            break
        sleep(1)


def morse_led(message, dry_run=False):
    assert len(message) <= LED_RANGE[-1]
    colour_map = {
        '.': "1FE0E0",
        '-': "1F4CE0",
        '/': "FFFFFF",
        ' ': "000000",
    }

    morse_msg = encode(message)
    for led_index, char in enumerate(morse_msg):
        update_led(led_index, colour_map[char], dry_run)
