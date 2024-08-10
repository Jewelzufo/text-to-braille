#press q to quit
def text_to_braille(text):
    """
    Convert text characters to Braille cells.

    Args:
        text (str): The text to convert.

    Returns:
        str: The Braille representation of the text.
    """
    # Define the Braille alphabet
    braille_alphabet = {
        'A': '⠊', 'B': '⠃', 'C': '⠉', 'D': '⠙', 'E': '⠑',
        'F': '⠋', 'G': '⠛', 'H': '⠓', 'I': '⠊⠑', 'J': '⠫',
        'K': '⠅', 'L': '⠇', 'M': '⠍', 'N': '⠝', 'O': '⠕',
        'P': '⠏', 'Q': '⠟', 'R': '⠗', 'S': '⠎', 'T': '⠞',
        'U': '⠥', 'V': '⠭', 'W': '⠭⠓', 'X': '⠭⠑', 'Y': '⠽',
        'Z': '⠵',
        ' ': '⠀',  # space
        ',': '⠂',  # comma
        '.': '⠲',  # period
        '?': '⠦',  # question mark
        '!': '⠖',  # exclamation mark
    }

    # Convert text to Braille
    braille_text = ''
    for char in text.upper():
        if char in braille_alphabet:
            braille_text += braille_alphabet[char]
        else:
            # Handle unknown characters
            braille_text += '⠿'  # unknown character symbol

    return braille_text

def main():
    print("Braille Converter")
    print("-----------------")

    while True:
        text = input("Enter text to convert to Braille (or 'q' to quit): ")
        if text.lower() == 'q':
            break
        braille_text = text_to_braille(text)
        print("Braille:", braille_text)

if __name__ == "__main__":
    main()