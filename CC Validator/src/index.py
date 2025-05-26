import re

def get_credit_card_flag(card_number: str) -> str:
    """
    Receives a credit card number as a string and returns its corresponding card flag (brand).
    Supported flags include: VISA, MASTERCARD, AMERICAN EXPRESS, DINERS CLUB, DISCOVER, ENROUTE, JCB, VOYAGER, HIPERCARD, and AURA.
    The function first removes all non-digit characters from the input, then validates the card number using the Luhn algorithm.
    If the card number is valid and matches a known flag pattern, the corresponding flag name is returned.
    If the card number is invalid or does not match any known flag, 'INVALID' is returned.
    Args:
        card_number (str): The credit card number to be checked.
    Returns:
        str: The detected card flag, or 'INVALID' if the card is not valid or not recognized.
    """
    card_number = re.sub(r'\D', '', card_number)

    def luhn_check(number):
        total = 0
        reverse_digits = number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    flags = [
        ("VISA",         r"^4\d{12}(\d{3})?$"),
        ("MASTERCARD",   r"^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$"),
        ("AMERICAN EXPRESS", r"^3[47]\d{13}$"),
        ("DINERS CLUB",  r"^3(0[0-5]|[68]\d)\d{11}$"),
        ("DISCOVER",     r"^6(011\d{12}|5\d{14}|4[4-9]\d{13})$"),
        ("ENROUTE",      r"^2(014|149)\d{11}$"),
        ("JCB",          r"^(2131|1800|35\d{3})\d{11}$"),
        ("VOYAGER",      r"^8699\d{11}$"),
        ("HIPERCARD",    r"^(606282\d{10}(\d{3})?|3841\d{15})$"),
        ("AURA",         r"^50(4175|4181|4193|4320|4389|4514|4576|5041|5066|5067|5090|6277|6362|6363|6504|6505|6509|6516|6550)\d{10,13}$"),
    ]

    if not luhn_check(card_number):
        return "INVALID"

    for flag, pattern in flags:
        if re.match(pattern, card_number):
            return flag

    return "INVALID"

# ...existing code...

if __name__ == "__main__":
    card_number = input("Enter a credit card number: ")
    flag = get_credit_card_flag(card_number)
    print(f"Card Flag: {flag}")