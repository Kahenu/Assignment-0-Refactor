def generate_pattern(square_count, printer):
    """ prepares pattern for printing """
    if square_count <= 0:
        return
    print('+', end='')
    for counter in range(square_count):
        print(printer(counter), end='')


def square_printer(counter):
    """ prints pattern """
    return f"-+\n{' ' * (counter * 2)}| |\n{' ' * (counter * 2)}+-+"


if __name__ == "__main__":
    sg = square_printer
    square_amount = int(input("Enter the number of squares: "))
    generate_pattern(square_amount, sg)
