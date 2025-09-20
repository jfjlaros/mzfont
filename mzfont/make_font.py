from .suppress import suppress_output

with suppress_output():
    from fontforge import font as ff_font
from fontforge import open as ff_open
from psMat import scale


def _read_glyphs(handle):
    '''
    '''
    return [handle.read(8) for _ in range(512)]


def _read_perm(handle):
    '''
    '''
    handle.seek(0x0a92)
    return handle.read(256)


class MzFont:
    '''
    '''
    def __init__(self, glyphs_handle, perm_handle, base_font, font_name):
        '''
        '''
        self._glyphs = _read_glyphs(glyphs_handle)
        self._perm = _read_perm(perm_handle)
        self._identity = range(256);
        self._dim = (5, 8)

        with suppress_output():
            self._font = ff_open(base_font)
        self._font.fontname = font_name
        self._font.familyname = font_name
        self._font.fullname = font_name
        self._font.em = 64
        self._font.ascent = 48
        self._font.descent = 0


    def _draw_pixel(self, pen, x, y):
        '''
        '''
        width, height = self._dim
        pen.moveTo((width * x, height * (6 - y)))
        pen.lineTo((width * (x + 1), height * (6 - y)))
        pen.lineTo((width * (x + 1), height * (5 - y)))
        pen.lineTo((width * x, height * (5 - y)))
        pen.closePath()

    def _make_character(self, code, glyph):
        '''
        '''
        char = self._font.createChar(code)
        char.width = self._dim[0]

        pen = char.glyphPen()
        for y in range(8):
            for x in range(8):
                if glyph[y] & (1 << x):
                    self._draw_pixel(pen, x, y)

    def _make_charset(self, offset, charset, perm):
        '''
        '''
        glyph_offset = 0x100 * charset;
        for code in range(0x100):
            self._make_character(
                offset + code, self._glyphs[glyph_offset + perm[code]])

    def _make_charsets(self):
        '''
        '''
        # Normal charset.
        self._make_charset(0xe000, 0, self._perm)
        # Alternative charset.
        self._make_charset(0xe100, 1, self._perm)
        # Normal charset without control characters.
        self._make_charset(0xe200, 0, self._identity)
        # Alternative charset without control characters.
        self._make_charset(0xe300, 1, self._identity)

    def _make_default_charset(self):
        '''
        '''
        for code in range(0x20, 0x5e):
            self._make_character(code, self._glyphs[self._perm[code]])
        for code in range(0x61, 0x7b):
            self._make_character(code, self._glyphs[0x20 + code])
        self._make_character(0x5e, self._glyphs[0xbe])
        self._make_character(0x5f, self._glyphs[0x3c])
        self._make_character(0x60, self._glyphs[0xa4])
        self._make_character(0x7b, self._glyphs[0xbc])
        self._make_character(0x7c, self._glyphs[0x35])
        self._make_character(0x7d, self._glyphs[0x40])
        self._make_character(0x7e, self._glyphs[0xa5])

    def make_font(self, ttf_font):
        '''
        '''
        self._make_charsets()
        self._font.generate(ttf_font)

    def make_default_font(self, ttf_font):
        '''
        '''
        self._font.ascent = 64
        self._dim = (8, 8)
        self._font.os2_typolinegap = 0
        self._font.os2_use_typo_metrics = True

        self._make_default_charset();
        self.make_font(ttf_font);


def make_font(glyphs_handle, perm_handle, base_font, ttf_font, font_name):
    '''
    '''
    mzfont = MzFont(glyphs_handle, perm_handle, base_font, font_name)
    mzfont.make_font(ttf_font);


def make_default_font(
        glyphs_handle, perm_handle, base_font, ttf_font, font_name):
    '''
    '''
    mzfont = MzFont(glyphs_handle, perm_handle, base_font, font_name)
    mzfont.make_default_font(ttf_font);
