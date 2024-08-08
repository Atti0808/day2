# Morse code dictionary
text_to_morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', 
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', 
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def text_to_morse(text):
    # Convert the text to uppercase to match the dictionary keys
    text = text.upper()
    # Initialize an empty string to store the Morse code
    morse_code = ''
    
    for char in text:
        if char in text_to_morse_code:
            morse_code += text_to_morse_code[char] + ' '
        elif char == ' ':
            morse_code += '  '  # Separate words with two spaces
        else:
            morse_code += '? '  # Unknown characters are replaced with '?'
    
    return morse_code

def main():
    # Get the input text from the user
    text = input("Enter text to convert to Morse code: ")
    # Convert the text to Morse code
    morse_code = text_to_morse(text)
    # Display the Morse code
    print("Morse Code:", morse_code)

if __name__ == "__main__":
    main()
