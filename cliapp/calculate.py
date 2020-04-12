import sys
import click


# @click.command()
def add(a, b):
    """Adds two numbers"""
    return a + b


def subtract(a, b):
    """Subtracts a number from another"""
    return a -b


def multiply(a, b):
    """Multiplies two numbers"""
    return a * b


def divide(a, b):
    """Simple division"""
    return a / b


@click.command()
@click.option('--func', '-f')
@click.argument('--anum', '-a', type=click.INT)
@click.argument('--bnum', '-b', type=click.INT)
def main(func, anum, bnum):

    switcher = {
        'add': add(anum, bnum),
        'subtract': subtract(anum, bnum),
        'multiply': multiply(anum, bnum),
        'divide': divide(anum, bnum)
    }
    print(switcher.get(func, 'Option does not exist'))
    #
    # print(add(anum, bnum))
    # print(subtract(anum, bnum))


if __name__ == '__main__':
    main()
