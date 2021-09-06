"""Chaitana's Colossal Coaster

https://exercism.org/tracks/python/exercises/chaitanas-colossal-coaster
"""


def add_me_to_the_queue(express_queue: list[str], normal_queue: list[str],
                        ticket_type: int, person_name: str) -> list[str]:
    """Add name to the correct queue

    Args:
        express_queue (list[str]): List of names in the express queue
        normal_queue (list[str]): List of names in the normal queue
        ticket_type (int): Ticket type (1 is express, 0 is normal)
        person_name (str): Name of person to add

    Returns:
        list[str]: The updated queue the name was added to
    """

    queue = express_queue if ticket_type == 1 else normal_queue
    return queue + [person_name]


def find_my_friend(queue: list[str], friend_name: str) -> int:
    """Find where a person is in the queue

    Args:
        queue (list[str]): List of names in the queue
        friend_name (str): Name of friend to find

    Returns:
        int: Index at which the friend was found
    """

    return queue.index(friend_name)


def add_me_with_my_friends(queue: list[str], index: int,
                           person_name: str) -> list[str]:
    """Add a new name to the queue at index position

    Args:
        queue (list[str]): List of names in the queue
        index (int): Index at which to add the new name
        person_name (str): The name to add

    Returns:
        list[str]: Queue with new name added
    """

    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    """Remove a name from a list

    Args:
        queue (list[str]): List of names in the queue
        person_name (str): Name of person to remove

    Returns:
        list[str]: Queue with name removed
    """

    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list[int], person_name: str) -> int:
    """Count how many people in list with exactly the same name

    Args:
        queue (list[int]): List of names in the queue
        person_name (str): Name to check for duplicates

    Returns:
        int: The number of times the name appears in the queue
    """

    return queue.count(person_name)


def remove_the_last_person(queue: list[str]) -> str:
    """Remove and return the last person from the queue

    Args:
        queue (list[str]): List of names in the queue

    Returns:
        str: The name removed from the end of the queue
    """

    return queue.pop()


def sorted_names(queue: str) -> list[str]:
    """Create a sorted copy of the queue

    Args:
        queue (str): List of names in the queue

    Returns:
        list[str]: A copy of the queue sorted in alphabetical order
    """

    return sorted(queue)
