from .chars import CHARS

# Returns the ANSI escape sequence for the given code.
sand = lambda code: '\033[' + str(code) + 'm'

def apply(text: str, *codes: str) -> str:
    """ Applies the given styles to the text. """

    # Combine the styles and text.
    style_ = ''.join(codes)
    reset = sand(CHARS['reset'])
    text_ = style_ + text + reset

    return text_

def style(*styles: str) -> lambda text: str:
    """ Returns a function that applies the given styles to the text. """

    # Get the ANSI escape sequences for the given styles.
    codes = [
        sand(
            sty[4:] if sty.startswith('CODE')
            else CHARS[sty]
        ) for sty in styles
    ]
    
    return lambda text: apply(text, *codes)