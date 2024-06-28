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

    if not styles:
        # No styles were given.
        return lambda text: text

    # Get the ANSI escape sequences for the given styles.
    codes = [
        sand(
            sty if isinstance(sty, int)             # The integer value
            else sty[4:] if sty.startswith('CODE')  # Predefined code
            else CHARS[sty]                         # User-input style
        ) for sty in styles
    ]
    
    # Return the lambda function responsible for applying those styles.
    return lambda text: apply(text, *codes)