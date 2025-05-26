# Credit Card Validator

This project is a simple Python utility to validate credit card numbers and identify their corresponding card flag (brand), such as VISA, MASTERCARD, AMERICAN EXPRESS, DINERS CLUB, DISCOVER, ENROUTE, JCB, VOYAGER, HIPERCARD, and AURA.

## Features

- **Credit Card Validation:** Uses the Luhn algorithm to check if a credit card number is valid.
- **Card Flag Detection:** Identifies the card brand based on the number pattern.
- **Command Line Interface:** Allows users to input a card number and receive instant feedback.

## How It Works

1. **Input:** The user enters a credit card number (with or without spaces/dashes).
2. **Sanitization:** All non-digit characters are removed.
3. **Validation:** The number is checked using the Luhn algorithm.
4. **Flag Detection:** The number is matched against known patterns for each supported card brand.
5. **Output:** The detected card flag is printed, or "INVALID" if the number is not valid or not recognized.

## Supported Card Flags

- VISA
- MASTERCARD
- AMERICAN EXPRESS
- DINERS CLUB
- DISCOVER
- ENROUTE
- JCB
- VOYAGER
- HIPERCARD
- AURA

## Usage

### Requirements

- Python 3.7 or higher

### Running the Validator

1. Clone this repository or download the source code.
2. Open a terminal and navigate to the project directory.
3. Run the following command:

    ```sh
    python src/index.py
    ```

4. Enter a credit card number when prompted.

### Example

```
Enter a credit card number: 4111 1111 1111 1111
Card Flag: VISA
```

## Project Structure

```
CC Validator/
├── prompts/
│   └── cc_prompt.md      # Promps used to create the files of this project
├── src/
│   └── index.py      # Main script with validation logic
└── README.md         # Project documentation
```

## How to Extend

- To add support for more card brands, add new patterns to the `flags` list in `index.py`.
- To integrate with other applications, import the `get_credit_card_flag` function from `src/index.py`.

## License

This project is licensed under the MIT License.

---

*Created for educational and demonstration purposes.*