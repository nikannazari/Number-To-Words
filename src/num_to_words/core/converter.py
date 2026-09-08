from num_to_words.core.constants import (
    SCALES,
    TENS,
    UNDER_20,
)


class NumberToWordsConverter:

    def convert(self, number: int) -> str:
        """
        Convert an integer into its English word representation.

        :param int number: Number to convert.
        :return: Number represented as words.
        :rtype: str
        """
        if number < 0:
            return "Negative " + self.convert(abs(number))

        if number < 1000:
            return self._convert_under_thousand(number)

        return self._convert_large_number(number)

    def _convert_under_thousand(self, number: int) -> str:
        if number < 20:
            return UNDER_20[number]

        if number < 100:
            return self._convert_two_digits(number)

        return self._convert_hundreds(number)

    def _convert_two_digits(self, number: int) -> str:
        tens = TENS[number // 10]
        remainder = number % 10

        if remainder == 0:
            return tens

        return f"{tens} {UNDER_20[remainder]}"

    def _convert_hundreds(self, number: int) -> str:
        hundreds = number // 100
        remainder = number % 100

        result = f"{UNDER_20[hundreds]} Hundred"

        if remainder:
            result += f" and {self._convert_under_thousand(remainder)}"

        return result

    def _convert_large_number(self, number: int) -> str:
        chunks = []
        scale_index = 0

        while number > 0:
            chunk = number % 1000

            if chunk:
                chunks.append(
                    (
                        chunk,
                        scale_index,
                        self._convert_under_thousand(chunk),
                    )
                )

            number //= 1000
            scale_index += 1

        if scale_index > len(SCALES):
            raise ValueError(
                "Number is too large to convert."
            )

        chunks.reverse()

        parts = []

        for chunk, index, words in chunks:
            if index > 0:
                words = f"{words} {SCALES[index]}"

            parts.append(words)

        result = " ".join(parts)

        last_chunk = chunks[-1][0]

        if len(chunks) > 1 and last_chunk < 100:
            result = result.replace(
                f" {self._convert_under_thousand(last_chunk)}",
                f" and {self._convert_under_thousand(last_chunk)}",
                1,
            )

        return result


def num_to_words(number: int) -> str:
    """
    Convert an integer into words.

    :param int number: Number to convert.
    :return: Word representation of the number.
    :rtype: str
    """
    converter = NumberToWordsConverter()

    return converter.convert(number)