# Stolen from https://gist.github.com/ebuckley/1842461

morse_ab = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}

morse_ab_inverted = dict((v, k) for (k, v) in morse_ab.items())

testCode = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- " \
           "-.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. " \
           ".- -.-- "


# parse a morse code string positionInString is the starting point for decoding
def decode(code, position=0):
    if position < len(code):
        morse_letter = ""
        for key, char in enumerate(code[position:]):
            if char == " ":
                position = key + position + 1
                letter = morse_ab_inverted[morse_letter]
                return letter + decode(code, position)

            else:
                morse_letter += char
    else:
        return ""


# encode a message in morse code, spaces between words are represented by '/'
def encode(message):
    message = ""
    for char in message[:]:
        message += morse_ab[char.upper()] + " "

    return message
