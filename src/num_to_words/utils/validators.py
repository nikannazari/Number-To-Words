def validate_number(
    number: int,
) -> bool:
    """
    Validate an integer input.

    :param int number: Number to validate.
    :return: True if valid.
    :rtype: bool
    """

    if not isinstance(number, int):

        raise TypeError(
            "Number must be an integer."
        )

    return True


def parse_number(
    value: str,
) -> int:
    """
    Convert a string input into an integer.

    :param str value: Input value.
    :return: Parsed integer.
    :rtype: int
    """

    value = value.strip()

    if not value:

        raise ValueError(
            "Number cannot be empty."
        )

    try:

        number = int(value)

    except ValueError:

        raise ValueError(
            "Invalid number. "
            "Please enter an integer."
        )

    return number