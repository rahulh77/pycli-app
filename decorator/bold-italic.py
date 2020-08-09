import typing
from functools import wraps

def htmltags(arg_tags):
    def decorator(func):
        def inner(*args, **kwargs):
            returned_value = func(*args, **kwargs)
            return '<'+arg_tags+'>' + returned_value + '</'+arg_tags+'>'
        return inner
    return decorator

def htmltags2(arg_tags):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            returned_value = func(*args, **kwargs)
            return '<'+arg_tags+'>' + returned_value + '</'+arg_tags+'>'
        return inner
    return decorator

@htmltags('b')
@htmltags('i')
def myfunc(input_str: str) -> str:
    """[Testing function with decorator arguments]

    Args:
        input_str (str): [Input string]

    Returns:
        str: [Output String]
    """
    print(input_str)
    return input_str

@htmltags2('b')
@htmltags2('i')
def myfunc2(input_str: str) -> str:
    """[Testing function with decorator arguments]

    Args:
        input_str (str): [Input string]

    Returns:
        str: [Output String]
    """
    print(input_str)
    return input_str

if __name__ == "__main__":
    x = myfunc('without functools wraps')
    print("The value of x is:", x)
    print("The wrapped functions docstring is:", myfunc.__doc__)
    print("The wrapped functions name is:", myfunc.__name__)
    print('\n')
    y = myfunc2('with functools wraps')
    print("The value of x is:", y)
    print("The wrapped functions docstring is: \n", myfunc2.__doc__)
    print("The wrapped functions name is:", myfunc2.__name__)
    # mismatched_words('My name is Rahul', 'What is your name')