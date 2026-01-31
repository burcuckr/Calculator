import day10logo
print(day10logo.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
first_num = float(input("What's the first number?: "))

should_accumulate = True
while should_accumulate:
    operation = input("+\n -\n *\n /\nPick an operation: ")
    second_num = float(input("What's the next number?: "))
    answer = operations[operation](first_num, second_num)
    print(f"{first_num} {operation}  {second_num} = {answer}")

    continue_ = input(f"Type 'y' to continue calculating with {answer} or 'n' to start new calculation: ")
    if continue_ == "y":
        first_num = answer
    else:
        break