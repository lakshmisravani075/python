# Fixed Code
if True:
    print("Hello - Fixed Syntax")


# 2. ZeroDivisionError
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


# 3. ValueError
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Error: Please enter a valid number!")


# 4. TypeError
try:
    x = 10
    y = "hello"
    print(x + y)   # Invalid
except TypeError:
    print("Error: Cannot add integer and string!")


# 5. Finally Block
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except Exception as e:
    print("Error occurred:", e)
finally:
    print("Program Completed")


# 6. Multiple Exceptions
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Please enter valid numbers!")


# 7. File Handling Error
try:
    f = open("student_data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: student_data.txt file not found!")


# 8. Catch All Exceptions
try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except Exception as e:
    print("Unexpected error:", e)


# 9. Custom Error Message
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Your age is:", age)
except ValueError as ve:
    print("Error:", ve)


# 10. Safe Calculator
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero!")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operator!")
except ValueError:
    print("Error: Please enter valid numbers!")
