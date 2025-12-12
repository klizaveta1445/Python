
import sys
import math

def input_coefficient(name, arg=None):
    while True:
        if arg is not None:
            value = arg
            arg = None  
        else:
            value = input(f"Введите коэффициент {name}: ")
        try:
            return float(value)
        except ValueError:
            print(f"Некорректное значение для {name}, введите ещё раз.")

def solve_biquadratic(a, b, c):
    
    discr = b**2 - 4*a*c 
    
    if discr < 0:
        return []  
    
    roots_y = []
    sqrt_discr = math.sqrt(discr)
    y1 = (-b + sqrt_discr) / (2*a)
    y2 = (-b - sqrt_discr) / (2*a)
    
    roots = []
    for y in [y1, y2]:
        if y < 0:
            continue  
        if y == 0:
            roots.append(0)
        else:
            roots.append(math.sqrt(y))
            roots.append(-math.sqrt(y))
    return sorted(set(roots))


args = sys.argv[1:]  

a = input_coefficient('А', args[0] if len(args) > 0 else None)
b = input_coefficient('В', args[1] if len(args) > 1 else None)
c = input_coefficient('С', args[2] if len(args) > 2 else None)

while a == 0:
    print("Коэффициент А не может быть 0 для биквадратного уравнения.")
    a = input_coefficient('А')

roots = solve_biquadratic(a, b, c)

if not roots:
    print("Действительных корней нет.")
else:
    print("Действительные корни уравнения:")
    for r in roots:
        print(r)


