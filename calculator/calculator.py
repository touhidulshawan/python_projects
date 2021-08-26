def take_input():
    try:
        input_numbers = [int(number) for number in input("Enter two numbers: ").split()]
        is_valid_input = validate_input(input_numbers)
        if is_valid_input:
            return input_numbers
        else:
            return take_input()
    except ValueError:
        print("Input should be separated by space")
        return take_input()


def validate_input(input_numbers):
    if len(input_numbers) != 2:
        print("Invalid number of inputs")
        is_valid = False
    else:
        is_valid = True
    return is_valid


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num1 > num2:
        return num1 / num2
    else:
        return num2 / num1


def print_result(res, operation):
    print(f"{operation} of given numbers = {res}")


exit_program = False

while not exit_program:
    print("""
	1. Addition
	2. Subtraction
	3. Multiplication
	4. division
	5. Exit Program
	"""
          )

    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        numbers = take_input()
        result = addition(numbers[0], numbers[1])
        print_result(result, "Addition")
    elif choice == 2:
        numbers = take_input()
        result = subtraction(numbers[0], numbers[1])
        print_result(result, "Subtraction")
    elif choice == 3:
        numbers = take_input()
        result = multiplication(numbers[0], numbers[1])
        print_result(result, "Multiplication")
    elif choice == 4:
        numbers = take_input()
        print(numbers)
        result = division(numbers[0], numbers[1])
        print_result(result, "Division")
    elif choice == 5:
        exit_program = True
    else:
        print("Invalid number of choice!!")
