import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:

    sys.path.insert(
        0,
        str(SRC_DIR),
    )


import streamlit as st

from num_to_words.core.converter import (
    num_to_words,
)
from num_to_words.utils.validators import (
    parse_number,
)


st.set_page_config(
    page_title="Number to Words",
    page_icon="🔢",
    layout="centered",
)


st.title("🔢 Number to Words")

st.write(
    "Convert an integer into English words."
)

st.divider()


number_input = st.text_input(
    "Enter a number",
    placeholder="123456",
)


if st.button(
    "Convert",
    use_container_width=True,
):

    try:

        number = parse_number(
            number_input
        )

        result = num_to_words(
            number
        )

        st.success("Conversion successful.")

        st.subheader("Result")

        st.code(
            result,
            language=None,
        )

    except (
        ValueError,
        TypeError,
    ) as error:

        st.error(
            str(error)
        )