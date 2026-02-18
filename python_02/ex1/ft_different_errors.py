def garden_operations()
    try:
        x = int("abc")
    except Exception as e:
        if type(e) == ValueError:
            print("Testing ValueError...")
            print("Caught ValueError: invalid literal for int()")
        elif type(e) == ZeroDivisionError:
            print("Testing ZeroDivisionError...")
            print("Caught ZeroDivisionError: division by zero")
        elif type(e) == FileNotFoundError
            print("Testing FileNotFoundError...")
            print("Caught FileNotFoundError: No such file 'missing.txt'")
        elif type(e) == KeyError:
            print("Testing KeyError...")
            print("Caught KeyError: 'missing\_plant'")
        else
            print("Testing multiple errors together...")
            print("Caught an error, but program continues!")
