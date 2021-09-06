"""Card Games

https://exercism.org/tracks/python/exercises/card-games
"""

from statistics import mean, median


def get_rounds(number: int) -> list[int]:
    '''

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    '''

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    '''

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    '''

    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    '''

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    '''

    return number in rounds


def card_average(hand: list[int]) -> float:
    '''

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    '''

    return mean(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    '''

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    '''

    full_avg = mean(hand)
    approx_avg_1 = mean([hand[0], hand[-1]])
    approx_avg_2 = median(hand)

    return full_avg in (approx_avg_1, approx_avg_2)


def average_even_is_average_odd(hand: list[int]) -> bool:
    '''

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    '''

    evn_avg = mean(hand[1::2])
    odd_avg = mean(hand[0::2])

    return evn_avg == odd_avg


def maybe_double_last(hand: list[int]):
    '''

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    '''

    last_card = hand[-1]
    last_is_jack = last_card == 11
    if last_is_jack:
        hand[-1] *= 2

    return hand
