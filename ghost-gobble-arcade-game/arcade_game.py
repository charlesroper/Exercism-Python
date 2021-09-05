"""Ghost Gobble Arcade Game

https://exercism.org/tracks/python/exercises/ghost-gobble-arcade-game
"""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Test if Pac-Man is able to eat ghost

    Args:
        power_pellet_active (bool): Does the player have an active power
            pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Is Pac-Man able to eat ghost?
    """

    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Test if Pac-Man scores

    Args:
        touching_power_pellet (bool): Is the player touching a power pellet?
        touching_dot (bool): Is the player touching a dot?

    Returns:
        bool: Does Pac-Man score?
    """

    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Test if Pac-Man loses

    Args:
        power_pellet_active (bool): Does the player have an active power
            pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Does Pac-Man die?
    """

    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots: bool, power_pellet_active: bool,
        touching_ghost: bool) -> bool:
    """Test if Pac-Man wins

    Args:
        has_eaten_all_dots (bool): Has Pac-Man eaten all the dots?
        power_pellet_active (bool): Does the player have an active power
            pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Does Pac-Man win?
    """

    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
