from .utils import style

class color:
    # Text colors.
    class t:
        k = style('kt0')
        r = style('rt0')
        g = style('gt0')
        y = style('yt0')
        b = style('bt0')
        m = style('mt0')
        c = style('ct0')
        w = style('wt0')
        d = style('dt0')

    # Background colors.
    class b:
        k = style('kb0')
        r = style('rb0')
        g = style('gb0')
        y = style('yb0')
        b = style('bb0')
        m = style('mb0')
        c = style('cb0')
        w = style('wb0')
        d = style('db0')

    # Bright text colors.
    class t_:
        k = style('kt1')
        r = style('rt1')
        g = style('gt1')
        y = style('yt1')
        b = style('bt1')
        m = style('mt1')
        c = style('ct1')
        w = style('wt1')

    # Bright background colors.
    class b_:
        k = style('kb1')
        r = style('rb1')
        g = style('gb1')
        y = style('yb1')
        b = style('bb1')
        m = style('mb1')
        c = style('cb1')
        w = style('wb1')