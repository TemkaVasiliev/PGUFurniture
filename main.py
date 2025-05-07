def parameters():
    def print_parameters(a, b, c, area, perimeter) -> None:
        print("\nВведенные параметры:")
        print("Длина первого катета: ", a)
        print("Длина второго катета: ", b)
        print("\nРезультаты вычислений:")
        print("Третья сторона прямоугольного треугольника:", c)
        print("Площадь прямоугольного треугольника: ", area)
        print("Периметр прямоугольного треугольника: ", perimeter, "\n")
    try:
        while True:
            try:
                a = int(input("Введите длину первого катета: "))
                b = int(input("Введите длину второго катета: "))
            except ValueError:
                print("Ошибка: введите целое число!\n")
                continue 
            
            c = (a**2 + b**2)**0.5
            area = round(0.5 * a * b, 2)
            perimeter = round(a + b + c, 2)

            print_parameters(a, b, c, area, perimeter)
    except KeyboardInterrupt:
        print("\n\nЗавершение программы")

if __name__ == "__main__":
    parameters()