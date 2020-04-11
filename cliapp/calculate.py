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
@click.option('--anum', '-a', type=click.INT)
@click.option('--bnum', '-b', type=click.INT)
def main(anum, bnum):
    print(add(anum, bnum))
    print(subtract(anum, bnum))


if __name__ == '__main__':
    main()
