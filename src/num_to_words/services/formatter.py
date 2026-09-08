class NumberFormatter:

    @staticmethod
    def format(
        words: str,
    ) -> str:
        """
        Format converted number words.

        :param str words: Converted number.
        :return: Formatted text.
        :rtype: str
        """

        return " ".join(
            words.strip().split()
        )