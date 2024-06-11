# Calculator

This is a simple calculator application built using Python's Tkinter library. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division. It also includes "Clear" and "Delete" buttons for better usability.

## Features

- Addition, Subtraction, Multiplication, and Division operations
- Clear button to clear the entire input
- Delete button to remove the last character
- User-friendly GUI resembling a traditional calculator

## Usage

1. Clone this repository or download the `calculator.py` file.
2. Run the `calculator.py` file using Python:

    ```sh
    python calculator.py
    ```

3. The calculator GUI will open. You can use the buttons to perform calculations.

## Code Overview

### Main Class

- **Calculator**: The main class that creates and manages the calculator's GUI.

### Methods

- **create_widgets**: Sets up the entry field, buttons, and their layout.
- **on_button_click**: Handles the logic when any of the digit or operation buttons are clicked.
- **clear**: Clears the entry field.
- **delete**: Deletes the last character in the entry field.

### GUI Components

- **Entry Field**: Displays the current input and results.
- **Buttons**: Includes digit buttons (`0-9`), operation buttons (`+`, `-`, `*`, `/`), and special buttons (`=`, `C`, `DEL`).

## Example

Below is an example of how to use the calculator:

1. Click `1`, `+`, `2`, and then `=` to perform the operation `1 + 2`. The result `3` will be displayed.
2. Click `C` to clear the entry field.
3. Click `5`, `*`, `3`, and then `=` to perform the operation `5 * 3`. The result `15` will be displayed.
4. Click `DEL` to remove the last digit or operator from the entry field.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## Other ways of creating a calculator

Calculator.py and gui.py are other ways of creating a calculator without the starndard graphical representation.
These are just to show other ways of calculating two or more numbers. 

---

Enjoy using the calculator!
