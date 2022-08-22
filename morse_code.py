# just to get rid of error codes.
MORSE_CODE = {
    '....': 'K'
}


def decode_morse(morse_code):
    # split at 3 space
    # split each word
    # make the conversion
    # join each word, then join into sentence
    words = [x.split(' ') for x in morse_code.strip().split('   ')]
    res = []
    for word in words:
        convert = [MORSE_CODE[i] for i in word]
        res.append(''.join(convert))
    return ' '.join(res)
