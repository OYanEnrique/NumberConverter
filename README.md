# NumberConverter
A simple Python command-line tool that converts an integer to its binary, octal, or hexadecimal representation based on user input.

# 🔢 Integer Base Converter

This is a simple command-line tool written in Python that converts an integer into different number system bases. The user provides an integer and then chooses to convert it to binary, octal, or hexadecimal.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `NumberConverter.py`).
3.  Open your terminal or command prompt and navigate to the file's directory.
4.  Run the script with the following command:
    ```sh
    python NumberConverter.py
    ```
5.  First, enter the integer you wish to convert and press Enter.
6.  Next, enter `1` for binary, `2` for octal, or `3` for hexadecimal, and press Enter to see the result.

## Features

* **User Input:** The program prompts the user for both the number to be converted and the desired conversion base.
* **Conversion Logic:** It uses Python's native, highly efficient functions for conversion:
    * `bin(number)` to convert to binary.
    * `oct(number)` to convert to octal.
    * `hex(number)` to convert to hexadecimal.
* **Output:** The program prints the converted number, which includes a prefix (`0b`, `0o`, or `0x`) to indicate the base of the result.
* **Error Handling:** A simple check is in place to inform the user if they select an invalid conversion option.
