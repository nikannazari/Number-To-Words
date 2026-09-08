import argparse

from num_to_words.core.converter import (
    num_to_words,
)
from num_to_words.utils.validators import (
    parse_number,
)


def main() -> None:

    parser = argparse.ArgumentParser(
        description="Convert numbers into words."
    )

    parser.add_argument(
        "number",
        nargs="?",
        help="Integer to convert.",
    )

    args = parser.parse_args()

    if args.number is not None:

        number = parse_number(
            args.number
        )

    else:

        user_input = input(
            "Enter your number: "
        )

        number = parse_number(
            user_input
        )

    result = num_to_words(number)

    print()
    print(result)


if __name__ == "__main__":

    main()