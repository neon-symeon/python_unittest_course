width = int(input('szerokość prostokąta: '))
height = int(input('wysokość prostokąta: '))

assert width > 0 and height > 0, 'Wartości muszą być dodatnie.'

area = width * height

print(f'Pole prostokąta wynosi: {area}.')

