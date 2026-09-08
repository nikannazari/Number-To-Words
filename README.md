# Num-to-Words

A modular Python application that converts integers into their English word representation.

The project provides both a command-line interface (CLI) and a Streamlit web interface.

## Features

* Convert positive and negative integers to English words
* Support numbers from units to very large scales
* Support scales such as:

  * Thousand
  * Million
  * Billion
  * Trillion
  * Quadrillion
  * Quintillion
  * Sextillion
  * Septillion
  * Octillion
  * Nonillion
  * Decillion
* British-style `and` formatting
* Input validation
* CLI interface
* Streamlit web interface
* Modular and maintainable architecture
* Easy to extend

## Example

Input:

```text
1234567
```

Output:

```text
One Million Two Hundred and Thirty Four Thousand Five Hundred and Sixty Seven
```

Negative numbers are also supported:

```text
-25
```

Output:

```text
Negative Twenty Five
```

## Project Structure

```text
Num-to-Words/
├── main.py
├── app/
│   └── streamlit_app.py
├── assets/
├── src/
│   └── num_to_words/
│       ├── __init__.py
│       ├── cli.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── constants.py
│       │   └── converter.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── formatter.py
│       └── utils/
│           ├── __init__.py
│           └── validators.py
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
└── requirements.txt
```

## Architecture

The application is divided into several layers:

### Core

Contains the main number-to-words conversion logic and constants.

```text
core/
├── constants.py
└── converter.py
```

### Services

Contains formatting-related functionality.

```text
services/
└── formatter.py
```

### Utils

Contains input validation and parsing utilities.

```text
utils/
└── validators.py
```

### CLI

Provides a command-line interface for converting numbers.

### Streamlit

Provides a graphical web interface for the application.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Num-to-Words.git
cd Num-to-Words
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Main Launcher

Run:

```bash
python main.py
```

You will see:

```text
==================================================
          Number to Words
==================================================

1. Start Streamlit
2. Run CLI
3. Exit
```

### CLI

You can run the CLI directly:

```bash
python -m src.num_to_words.cli 123456
```

Or, if the package is installed/configured in your environment:

```bash
python -m num_to_words.cli 123456
```

You can also run the CLI without providing a number:

```bash
python -m src.num_to_words.cli
```

Then enter the number interactively.

### Streamlit

Run:

```bash
streamlit run app/streamlit_app.py
```

Or use:

```bash
python main.py
```

and select:

```text
1. Start Streamlit
```

## Examples

```text
0
→ Zero
```

```text
21
→ Twenty One
```

```text
100
→ One Hundred
```

```text
101
→ One Hundred and One
```

```text
1234
→ One Thousand Two Hundred and Thirty Four
```

```text
123456
→ One Hundred and Twenty Three Thousand Four Hundred and Fifty Six
```

```text
1000000
→ One Million
```

```text
1234567
→ One Million Two Hundred and Thirty Four Thousand Five Hundred and Sixty Seven
```

```text
-25
→ Negative Twenty Five
```

## Technologies

* Python
* Streamlit
* Setuptools

## Requirements

* Python 3.10+
* pip

## Version

Current version:

```text
1.1.0
```

## License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

## Author

Nikan Nazari
