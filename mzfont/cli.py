#!/usr/bin/python

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, FileType

from . import doc_split, usage, version
from .make_font import make_font, make_default_font


def _arg_parser() -> object:
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'glyphs_handle', metavar='CG', type=FileType('rb'),
        help='character rom file')
    parser.add_argument(
        'perm_handle', metavar='MONITOR', type=FileType('rb'),
        help='monitor rom file')
    parser.add_argument(
        'ttf_font', metavar='TTF', type=str, help='output file')
    parser.add_argument(
        '-b', dest='base_font', metavar='BASE', type=str,
        default='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
        help='base font file')
    parser.add_argument(
        '-n', dest='font_name', metavar='NAME', type=str, default='SharpMZ',
        help='font name')
    return parser


def main():
    parser = _arg_parser()

    try:
        args = parser.parse_args()
    except IOError as error:
        parser.error(error)

    make_font(
        args.glyphs_handle, args.perm_handle, args.base_font, args.ttf_font,
        args.font_name)


if __name__ == '__main__':
    main()
