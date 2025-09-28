from argparse import RawDescriptionHelpFormatter, ArgumentParser, FileType

from . import __copyright__, __description__, __info__, doc_split
from .make_font import MzFont
from .test_font import print_charsets


def make_font(glyphs_handle, perm_handle, base_font, ttf_font, font_name):
    mzfont = MzFont(glyphs_handle, perm_handle, base_font, font_name)
    mzfont.make_font(ttf_font)


def make_default_font(
        glyphs_handle, perm_handle, base_font, ttf_font, font_name):
    mzfont = MzFont(glyphs_handle, perm_handle, base_font, font_name)
    mzfont.make_default_font(ttf_font)


def _arg_parser():
    make_parser = ArgumentParser(add_help=False)
    make_parser.add_argument(
        'glyphs_handle', metavar='CG', type=FileType('rb'),
        help='character rom file')
    make_parser.add_argument(
        'perm_handle', metavar='MONITOR', type=FileType('rb'),
        help='monitor rom file')
    make_parser.add_argument(
        'ttf_font', metavar='TTF', type=str,
        help='output file')
    make_parser.add_argument(
        '-b', dest='base_font', metavar='BASE', type=str,
        default='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
        help='base font file')
    make_parser.add_argument(
        '-n', dest='font_name', metavar='NAME', type=str, default='SharpMZ',
        help='font name')

    parser = ArgumentParser(
        description = __description__, epilog=__copyright__,
        formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument(
        '-v', action='version', version=__info__)
    subparsers = parser.add_subparsers(dest='subcommand')
    subparsers.required = True

    make_font_parser = subparsers.add_parser(
        'make', parents=[make_parser], description=doc_split(MzFont.make_font))
    make_font_parser.set_defaults(func=make_font)

    make_default_font_parser = subparsers.add_parser(
        'default', parents=[make_parser],
        description=doc_split(MzFont.make_default_font))
    make_default_font_parser.set_defaults(func=make_default_font)

    test_font_parser = subparsers.add_parser(
        'test', description=doc_split(print_charsets))
    test_font_parser.set_defaults(func=print_charsets)

    return parser


def main():
    parser = _arg_parser()

    try:
        args = parser.parse_args()
    except IOError as error:
        parser.error(error)

    try:
        args.func(**{
            k: v for k, v in vars(args).items()
            if k not in ('func', 'subcommand')})
    except ValueError as error:
        parser.error(error)
