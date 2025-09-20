#!/usr/bin/python

from sys import stdout


def print_charset(offset):
    '''
    '''
    for index in range(256):
        stdout.write(f'{chr(0xE000 + offset + index)}')
        if index % 16 == 15:
            stdout.write('\n')


def print_charsets():
    '''
    '''
    for offset in [0x0000, 0x0100, 0x0200, 0x0300]:
        print_charset(offset)
        stdout.write('\n')


if __name__ == '__main__':
    print_charsets()
