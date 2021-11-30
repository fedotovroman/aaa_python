"""Morse Code Translator"""
import doctest

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}



def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    Test description: This test verifies the operation of the method for
    decoding string expressions from Morse code to English.

    doctests:

    >>> encode('MAI-PYTHON-2019')
    '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'

    >>> encode('HELLO-FROM-ACADEMY')
    '.... . .-.. .-.. --- -....- ..-. .-. --- -- -....- .- -.-. .- -.. . -- -.--'

    >>> encode('SOS')
    '... --- ...'

    >>> encode('Привет-из-академии!') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    KeyError:

    >>> encode('WINTER2021') # doctest: +ELLIPSIS
    '.--...'

    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == '__main__':
    doctest.testmod()
