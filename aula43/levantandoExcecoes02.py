def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log', error)
        raise


try:
    print(divide(10, 0))
except ZeroDivisionError as error:
    print(error)
