# author: Michael Hrenko
# Sources:
#   https://www.rapidtables.com/convert/color/rgb-to-hsv.html
#   https://www.rapidtables.com/convert/color/hsv-to-rgb.html

def RGB_to_HSV( arr_in ):

    R, G, B = arr_in[0] / 255., arr_in[1] / 255., arr_in[2] / 255.

    C_MIN = min(R, G, B)
    C_MAX = max(R, G, B)
    C_DIFF = C_MAX - C_MIN

    # Determine H
    if C_DIFF == 0:
        H = 0
    elif C_MAX == R:
        H = 60 * ( ((G-B) / C_DIFF ) % 6 )
    elif C_MAX == G:
        H = 60 * ( ((B-R) / C_DIFF ) + 2 )
    elif C_MAX == B:
        H = 60 * ( ((R-G) / C_DIFF ) + 4 )
    
    if H < 0:
        H += 360

    # Determine S   
    if C_MAX == 0:
        S = 0
    else:
        S = ( C_DIFF / C_MAX )

    # Determine V
    V = C_MAX

    # HSV Array
    arr_out = [int(H), round(S,3), round(V,3)]

    return arr_out

def HSV_to_RGB( arr_in ):

    H, S, V = arr_in[0], arr_in[1], arr_in[2]

    C = V * S
    m = V - C
    X = C * (1 - abs( (H / 60) % 2 - 1) )

    if H < 60:
        R, G, B = (C + m) * 255, (X + m) * 255, (0 + m) * 255 
    elif 60 <= H < 120:
        R, G, B = (X + m) * 255, (C + m) * 255, (0 + m) * 255
    elif 120 <= H < 180:
        R, G, B = (0 + m) * 255, (C + m) * 255, (X + m) * 255
    elif 180 <= H < 240:
        R, G, B = (0 + m) * 255, (X + m) * 255, (C + m) * 255
    elif 240 <= H < 300:
        R, G, B = (X + m) * 255, (0 + m) * 255, (C + m) * 255
    elif 300 <= H:
        R, G, B = (C + m) * 255, (0 + m) * 255, (X + m) * 255
    
    # RGB array
    arr_out = [int(R), int(G), int(B)]

    return arr_out