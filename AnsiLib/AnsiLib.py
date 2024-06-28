from typing import List
from typing import Literal

from .chars import CHARS

# Colours class.
from .color import color as c

# Styling function.
from .utils import style

# Quick styles.
s = style('s')
d = style('d')
i = style('i')
u = style('u')
k = style('k')
h = style('h')
x = style('x')
du = style('du')
rev = style('rev')

# Quick colours.
r = style('r')
g = style('g')
y = style('y')
b = style('b')
m = style('m')
cy = style('c')
w = style('w')

def available() -> List[str]:
    """ Returns the available styles. """

    # Get the available styles.
    ints: dict = {v: None for v in set(CHARS.values())}
    for sty in CHARS.keys():
        i: int = CHARS[sty]
        if i in ints.keys() and not ints[i]:
            ints[i] = sty
    
    names = list(ints.values())
    return names

def color(r: int, g: int, b: int, type: str = 'fg') -> str:
    """ Returns the ANSI escape sequence for the given RGB colour. """
    # Set the type.
    type = '38' if type == 'fg' else '48'
    
    # Generate the ANSI escape sequence.
    code = f'CODE{type};2;{r};{g};{b}'
    
    return code

def prints(
    *values: object,
    style: List[str] | callable | None = None,
    sep: str | None = " ",
    end: str | None = "\n",
    file = None,
    flush: Literal[False] = False
) -> None:
    """ Prints the given values with the given style. """

    # Get the style.
    style_ = None

    if not style:
        # No style was given.
        style_ = globals()['style']()
    elif isinstance(style, list) or isinstance(style, tuple) or isinstance(style, set):
        # The style is an array.
        style_ = globals()['style'](*style)
    elif callable(style):
        # The style is a function.
        style_ = style
    else:
        # Invalid style.
        raise TypeError('Style must be an array or a function.')

    # Apply the style.
    text = style_(
        sep.join([str(v) for v in values])
    )

    # Print the text.
    print(text, end=end, file=file, flush=flush)