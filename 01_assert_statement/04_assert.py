"""
Przykłady asercji funkcji.
"""


def area(width, height):
    return width * height + 1


assert area(4, 5) == 20, 'Prostokąt 4 x 5 ma pole 20'
