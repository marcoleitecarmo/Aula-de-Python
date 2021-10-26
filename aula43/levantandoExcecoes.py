# https://docs.python.org/3/library/exceptions.html

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)


print(divide(9, 0))
