# 5. Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction
from math import gcd, lcm



def main():
    first: list[str] = []
    second: list[str] = []
    sum_of_frac: list[int] = [0, 0]
    mulp: list[int] = [0, 0]
    great: int = 0
    less: int = 0

    try:
        first = (str(input("Please enter first fraction.\n"))).split("/")
        if len(first) != 2:
            raise ValueError
        second = (str(input("Please enter second fraction.\n"))).split("/")
        if len(second) != 2:
            raise ValueError
    except ValueError:
        print("Incorrect data was entered.")
        main()

    less = lcm(int(first[1]), int(second[1]))

    sum_of_frac[0] = int(int(first[0]) * (less / int(first[1])) + int(second[0]) * (less / int(second[1])))
    sum_of_frac[1] = int(int(first[1]) * (less / int(first[1])))

    great = gcd(sum_of_frac[0], sum_of_frac[1])
    if great != 1:
        for i in range(len(sum_of_frac)):
            sum_of_frac[i] /= great

    for i in range(len(mulp)):
        mulp[i] = int(first[i]) * int(second[i])
    great = gcd(mulp[0], mulp[1])
    if great != 1:
        for i in range(len(mulp)):
            mulp[i] /= great

    print(f"Sum of two fractions is:\n"
          f"{sum_of_frac[0]}/{sum_of_frac[1]}\n"
          f"Multiplication of two fractions is:\n"
          f"{mulp[0]}/{mulp[1]}\n"
          f"In-built functions:\n"
          f"{Fraction(int(first[0]),int(first[1])) + Fraction(int(second[0]),int(second[1]))}\n"
          f"{Fraction(int(first[0]),int(first[1])) * Fraction(int(second[0]),int(second[1]))}")

    return 0


if __name__ == "__main__":
    main()
