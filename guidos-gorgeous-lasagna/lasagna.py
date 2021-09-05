"""Guido's Gorgeous Lasagne Exercism exercise

The first exercise in the Python track on Exercism. This exercise makes use of
constants, type annotations, and docstrings. The docstrings in the original look
like they are using the reStructuredText docstring style:

http://daouzli.com/blog/docstring.html#restructuredtext

But I prefer the Google style docstrings - I find the much more readable at a
glance:

https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings

So I will be using the Google style from here on.

Google style does not require declaring types in the docstring if we are using
type annotations. However, I don't see including them as doing any harm, and the
Python Docstring Generator for VS Code adds them by default, so I will include
them.
"""

# The numbers assigned to these constants represent minutes
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER_IN_MINUTES = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculates remaining cooking time of the lasagne

    Args:
        elapsed_bake_time (int): The number of minutes that have elapsed since
            baking was started.

    Returns:
        int: The remaining bake time in minutes
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculates the preparation time in minutes

    The initial preparation time of a lasagne - not to be confused with the
    cooking time of a lasagne - can be calculated by multiplying the prep time
    per layer as defined by the `PREPARATION_TIME_PER_LAYER_IN_MINUTES` constant
    and multiplying that by the number of layers we are using.

    Args:
        number_of_layers (int): The number of layers we are using in the
            lasagne

    Returns:
        int: The total initial preparation time of the lasagne
    """
    return PREPARATION_TIME_PER_LAYER_IN_MINUTES * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculates how long we have been making lasagne

    The calculation takes into account initial preparation time, and the amount
    of time we have spent baking so far.

    Args:
        number_of_layers (int): The number of layers in the pasta
        elapsed_bake_time (int): The number of minutes the lasagne has been in
            the over for

    Returns:
        int: The number of minutes we have been preparing and baking lasagne
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
