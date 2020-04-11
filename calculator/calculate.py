import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a -b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


if __name__ == '__main__':
    print(sys.argv)
    print(add(10, 8))
    print(subtract(5, 3))
