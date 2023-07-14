# 2. Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. 
# >* Диаметр не превышает 1000 у.е. 
# >* Точность вычислений должна составлять не менее 42 знаков после запятой.
from math import pi
_PI = pi.__round__(42)


def calculate(d: int) -> list[float]:
    return [_PI * ((d/2)**2), _PI*d]


def main():
    d: int = 0
    foo: list[float] = []
    print("Program is running")
    try:
        d = int(input("Enter diameter\n"))
        if d <= 0:
            raise ValueError
    except ValueError:
        print("Error! Please enter only valid numbers.")

    foo = calculate(d)
    print(f"Area is: {foo[0]}\nCircumference is: {foo[1]}")
    return 0


if __name__ == "__main__":
    main()
