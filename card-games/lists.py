"""Card Games

https://exercism.org/tracks/python/exercises/card-games
"""

# We're using Python 3.4 or greater, so we can use the statistics module
from statistics import mean, median


def get_rounds(number: int) -> list[int]:
    """Generate a list of three rounds

    Args:
        number (int): The number of the first round

    Returns:
        list[int]: A list of three rounds
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two rounds together

    Args:
        rounds_1 (list[int]): A list of rounds
        rounds_2 (list[int]): Another list of rounds

    Returns:
        list[int]: The two list of rounds joined together
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if number is a recent round

    Args:
        rounds (list[int]): A list of recent round numbers
        number (int): The number to check

    Returns:
        bool: True if the round has been played recently
    """

    return number in rounds


def card_average(hand: list[int]) -> float:
    """Average value of all cards in hand

    Args:
        hand (list[int]): The hand of cards

    Returns:
        float: The average value
    """

    return mean(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Check if approximate averages are same as full average

    Args:
        hand (list[int]): The hand of cards

    Returns:
        bool: True if approximate average is same as full average
    """

    approx_avg_1 = mean([hand[0], hand[-1]])
    approx_avg_2 = median(hand)

    return card_average(hand) in (approx_avg_1, approx_avg_2)


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Check if average of evens is same as average of odds

    Args:
        hand (list[int]): The hand of cards

    Returns:
        bool: True is evens are same as odds
    """

    evn_avg = mean(hand[1::2])
    odd_avg = mean(hand[0::2])

    return evn_avg == odd_avg


def maybe_double_last(hand: list[int]) -> list[int]:
    """Double the last value in the hand if it is a Jack (11)

    Args:
        hand (list[int]): The hand of cards

    Returns:
        list[int]: The hand of cards with last Jack doubled
    """

    last_is_jack = hand[-1] == 11
    if last_is_jack:
        hand[-1] *= 2

    return hand
