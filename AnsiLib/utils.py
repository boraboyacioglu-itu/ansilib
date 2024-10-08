from typing import Callable, List, Optional, Union
import warnings

from .chars import CHARS

# Returns the ANSI escape sequence for the given code.
sand: Callable[[object], str] = lambda code: '\x1b[' + str(code) + 'm'

def apply(text: object, *codes: str, p: bool = False) -> Optional[str]:
    """ Applies the given styles to the text.

    Args:
        text (object): The text to style.
        *codes (str): The styles to apply to the text.
        p (bool): Whether to print the text. (defaults to False)

    Returns:
        Optional[str]: The styled text if p is False.
    """

    # Check if codes only contains strings.
    if not all(isinstance(c, str) for c in codes):
        raise TypeError("Codes must be strings.")

    # Combine the styles and text.
    style_: str = ''.join(codes)
    reset: str = sand(CHARS['reset'])
    text_: str = style_ + str(text) + reset

    if not p:
        # Return the text.
        return text_
    
    print(text_)
    return None

def style(*styles: Union[int, Callable[[str, bool], str], str], p: bool = False) -> Callable[[str, bool], str]:
    """ Returns a function that applies the given styles to the text.

    Args:
        *styles (Union[int, Callable[[str, bool], str], str]): The styles to apply to the text.
        p (bool): Whether to print the text. (defaults to False)

    Returns:
        Callable[[str, bool], str]: The function that applies the styles to the text.
    """

    if not styles:
        # No styles were given.
        return lambda text, p=p: text
    
    # Convert the styles to a list.
    styles_: List[Union[int, Callable[[str, bool], str], str]] = list(styles)

    # Get the ANSI escape sequences for the given styles.
    codes: List[str] = []
    for sty in styles_:
        
        # The integer value.
        if isinstance(sty, int):
            if sty not in CHARS.values():
                warnings.warn("Style with escape code " + str(sty) + " may not be recognized.", UserWarning)
            codes.append(str(sty))

        elif callable(sty):
            # Remove sty from the styles.
            styles_.remove(sty)

            # Return the style with the function.
            style_func: Callable[[str, bool], str] = lambda text, p=p: sty(style(*styles_, p=p)(text))
            return style_func
        
        elif not isinstance(sty, str):
            raise TypeError("Style " + sty + " must be an integer, a string, or a callable.")

        # Predefined code.
        elif sty.startswith('CODE'):
            codes.append(sty[4:])
        
        # User-input style.
        else:
            if sty not in CHARS.keys():
                raise ValueError(f"Style '{sty}' is not recognized.")
            codes.append(str(CHARS[str(sty).lower()]))
    
    codes = [sand(c) for c in codes]
    
    # Return the lambda function responsible for applying those styles.
    style_func: Callable[[str, bool], str] = lambda text, p=p: apply(text, *codes, p=p)
    return style_func