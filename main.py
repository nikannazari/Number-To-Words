import subprocess
import sys


def main() -> None:

    print("=" * 50)
    print("          Number to Words")
    print("=" * 50)
    print()

    print("1. Start Streamlit")
    print("2. Run CLI")
    print("3. Exit")
    print()

    choice = input(
        "Select an option: "
    ).strip()

    if choice == "1":

        subprocess.run(
            [
                sys.executable,
                "-m",
                "streamlit",
                "run",
                "app/streamlit_app.py",
            ]
        )

    elif choice == "2":

        subprocess.run(
            [
                sys.executable,
                "-m",
                "num_to_words.cli",
            ]
        )

    elif choice == "3":

        print("Goodbye!")

    else:

        print("Invalid option.")


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\nGoodbye!")