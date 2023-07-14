# 1. Напишите программу, которая получает целое число и возвращает 
# его двоичное, восьмеричное и шестинадцеричное строковое представление.
class Base:
    @staticmethod
    def dec_to_bin(num: int) -> str:
        num_str = ""

        # Base cases
        if num == 0:
            for i in range(8):
                num_str += f"{0}"
        elif num == 1:
            for i in range(7):
                num_str += f"{0}"
            num_str += f"{1}"
        # Main case
        else:
            while num != 1:
                if num % 2 == 0:
                    num_str += f"{0}"
                    num /= 2
                else:
                    num_str += f"{1}"
                    num //= 2
            num_str += f"{1}"
            num_str = num_str[::-1]
        return num_str

    @staticmethod
    def dec_to_oct(num: int) -> str:
        num_str: str = ""
        octagonal: list[int] = [i for i in range(8)]
        # Base case
        if num in octagonal:
            num_str += f"{num}"
        # Main case
        else:
            while num not in octagonal:
                num_str += f"{num % 8}"
                num //= 8
            num_str += f"{num}"
            num_str = num_str[::-1]
        return num_str

    @staticmethod
    def dec_to_hex(num: int) -> str:
        h_dict: dict[int: str] = {10: "a", 11: "b", 12: "c",
                                  13: "d", 14: "e", 15: "f"}
        num_str: str = ""

        # Base case
        if num in range(0, 16):
            if h_dict.get(num) is not None:
                return h_dict[num]
            else:
                return f"{num}"
        else:
            while num not in range(0, 16):
                if h_dict.get(num % 16) is not None:
                    num_str += f"{h_dict.get(num % 16)}"
                else:
                    num_str += f"{num % 16}"
                num //= 16
            if h_dict.get(num % 16) is not None:
                num_str += f"{h_dict.get(num)}"
            else:
                num_str += f"{num}"
            num_str = num_str[::-1]
        return num_str


def main():
    num_int: int = 0

    print("Program is running!")

    try:
        num_int = int(input("Enter a number to convert.\n"))
    except ValueError:
        print("Error!\nPlease enter a valid number.")
        main()

    if num_int < 0:
        num_int *= -1

    print(f"Function: 0b{Base.dec_to_bin(num_int)}\n"
          f"In-built function: {bin(num_int)}")

    print(f"Function: 00{Base.dec_to_oct(num_int)}\n"
          f"In-built function: {oct(num_int)}")

    print(f"Function: 0x{Base.dec_to_hex(num_int)}\n"
          f"In-built function: {hex(num_int)}")

    return 0


if __name__ == "__main__":
    main()
