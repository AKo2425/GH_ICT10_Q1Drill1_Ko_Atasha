# The area of a trapezoid
from pyscript import display, document


def area_trapezoid(e):
    document.getElementById('output').innerHTML = ""
    num1 = float(document.getElementById('num1').value)
    num2 = float(document.getElementById('num2').value)
    num3 = float(document.getElementById('num3').value)

    display (f'The area of this trapezoid is {(num1 + num2) / 2 * num3} ,YAY!', target='output')
