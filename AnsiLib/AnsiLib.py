from typing import Dict

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

def available() -> Dict[int, str]:
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