from sys import stdout


def print_charset(offset: int) -> None:
    '''Print a character set.

    :arg offset: Character set offset relative to 0xe000.
    '''
    for index in range(256):
        stdout.write(f'{chr(0xe000 + offset + index)}')
        if index % 16 == 15:
            stdout.write('\n')


def print_charsets() -> None:
    '''Print all character sets.'''
    for offset in [0x0000, 0x0100, 0x0200, 0x0300]:
        print_charset(offset)
        stdout.write('\n')
