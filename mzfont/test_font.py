from sys import stdout


def print_charset(offset: int) -> None:
    '''Print a character set.

    :arg offset: Character set offset relative to 0xe000.
    '''
    for index in range(256):
        stdout.write(f'{chr(offset + index)}')
        if index % 16 == 15:
            stdout.write('\n')


def print_charsets() -> None:
    '''Print all character sets.'''
    print('Interchange character set:')
    print_charset(0xe000)
    print('\nPrimary display character set:')
    print_charset(0xe100)
    print('\nAlternate display character set:')
    print_charset(0xe200)
