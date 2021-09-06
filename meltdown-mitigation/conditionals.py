"""Meltdown Mitigation

https://exercism.org/tracks/python/exercises/meltdown-mitigation
"""


def is_criticality_balanced(temperature: int,
                            neutrons_emitted: int) -> bool:
    """Test to see if the reactor is critically balanced

    The reactor is critically balanced when:

    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than
      500_000.

    Args:
        temperature (int): The temperature of the reactor
        neutrons_emitted (int): The number of neurons emitted per second

    Returns:
        bool: Is the reactor critically balanced
    """

    product_of_temperature_and_neutrons = temperature * neutrons_emitted

    return (temperature < 800
            and neutrons_emitted > 500
            and product_of_temperature_and_neutrons < 500_000)


def reactor_efficiency(voltage: int,
                       current: int,
                       theoretical_max_power: int) -> str:
    """Calculate reactor efficiency band

    Once the reactor has started producing power its efficiency needs to be
    determined. Efficiency can be grouped into 4 bands:

    1. green  ->   80-100% efficiency
    2. orange ->   60-79% efficiency
    3. red    ->   30-59% efficiency
    4. black  ->   <30% efficient

    These percentage ranges are calculated as `(generated power / theoretical
    max power) * 100` where `generated power = voltage * current`

    Args:
        voltage (int): The reactor's voltage
        current (int): The reactor's current
        theoretical_max_power (int): The reactor's theoretical max power

    Returns:
        str: The efficiency band colour
    """

    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    # Use interval comparison
    # https://stackoverflow.com/questions/24436150/how-does-interval-comparison-work
    if 80 <= efficiency <= 100:
        return "green"
    if 60 <= efficiency <= 79:
        return "orange"
    if 30 <= efficiency <= 59:
        return "red"
    return "black"


def fail_safe(temperature: int,
              neutrons_produced_per_second: int,
              threshold: int) -> str:
    """Failsafe mechanism

    If temperature * neutrons_produced_per_second < 40% of threshold, output a
    status code of 'LOW' indicating that control rods must be removed to
    produce power.

    If temperature * neutrons_produced_per_second are within plus or minus 10%
    of the threshold the reactor is in criticality and the status code of
    'NORMAL' should be output, indicating that the reactor is in optimum
    condition and control rods are in an idea position.

    If temperature * neutrons_produced_per_second is not in the above-stated
    ranges, the reactor is going into meltdown and a status code of 'DANGER'
    must be passed to immediately shut down the reactor.


    Args:
        temperature (int): Temperature of reactor
        neutrons_produced_per_second (int): Number of neutrons the reactor is
            producing per second
        threshold (int): The reactor criticality threshold

    Returns:
        str: Status code
    """

    temp_and_neutrons = temperature * neutrons_produced_per_second
    percent_of_threshold_40 = 0.4 * threshold
    percent_of_threshold_10 = 0.1 * threshold
    normal_lbound = threshold - percent_of_threshold_10
    normal_ubound = threshold + percent_of_threshold_10

    if temp_and_neutrons < percent_of_threshold_40:
        return "LOW"
    if normal_lbound <= temp_and_neutrons <= normal_ubound:
        return "NORMAL"
    return "DANGER"
