
def division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as zerodv:
        print("you can not divide by 0!")
        print("Error:", zerodv)
    except (NameError, TypeError) as err:
        print("Check your input")
        raise err
    finally:
        print("finally block is executed")

division(45, 15)
division(45, 10)
division(100, 10)
division(45, 0)

filename = 'dat/inputData.txt'
try:
    with open(filename, 'a') as file_object:
        print("2. Reading the whole content and assigning to a variable")
except Exception as err:
    print(err)

division(60, "hello")