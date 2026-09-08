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
            result += " and " + self._convert_under_thousand(remainder)

        return result

    def _convert_large_number(self, number: int) -> str:
        chunks = []

        scale_index = 0

        while number > 0:
            chunk = number % 1000

            if chunk:
                chunk_words = self._convert_under_thousand(chunk)

                if scale_index > 0:
                    chunk_words += f" {SCALES[scale_index]}"

                chunks.append(chunk_words)

            number //= 1000
            scale_index += 1

        chunks.reverse()

        result = " ".join(chunks)

        return self._add_and(result, chunks)

    def _add_and(self, result: str, chunks: list[str]) -> str:
        """
        Add 'and' according to British English number formatting.
        """
        if len(chunks) < 2:
            return result

        last_chunk = chunks[-1]

        last_chunk_number = self._extract_chunk_number(last_chunk)

        if last_chunk_number < 100:
            parts = result.rsplit(" ", len(last_chunk.split()) - 1)

            if len(parts) > 1:
                prefix = " ".join(parts[:-1])
                suffix = parts[-1]
                return f"{prefix} and {suffix}"

        return result

    @staticmethod
    def _extract_chunk_number(chunk: str) -> int:
        """
        Convert the final numeric chunk back to an approximate integer
        for deciding whether 'and' is needed.
        """
        words = chunk.split()

        if not words:
            return 0

        if "Hundred" in words:
            return 100

        for index, word in enumerate(UNDER_20):
            if word in words:
                return index

        for index, word in enumerate(TENS):
            if word in words:
                return index * 10

        return 0


def num_to_words(number: int) -> str:
    """
    Convert an integer into words.

    :param int number: Number to convert.
    :return: Word representation of the number.
    :rtype: str
    """
    converter = NumberToWordsConverter()

    return converter.convert(number)