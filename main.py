from ascii_art import title, separator
import pyperclip

# This program's aim is to CONVERT Text to MORSE CODE and viceversa

# ---------------------- Switching the MORSE dict to obtain a Letter dict-------------------------------
# To switch the keys and values from MORSE_CODE_DICT and get a new dictionary of letter, so it's easier to
# translate from Morse to text, basically using the same function
# for k, v in MORSE_CODE_DICT.items():
#     LETTERS_DICT[v] = k
# print(LETTERS_DICT)

# ---------------------- MORSE CODE DICT and LETTER DICT-------------------------------
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}
LETTERS_DICT = {'.-': 'A', '-...': 'B',
                '-.-.': 'C', '-..': 'D',
                '.': 'E', '..-.': 'F', '--.': 'G',
                '....': 'H', '..': 'I', '.---': 'J',
                '-.-': 'K', '.-..': 'L', '--': 'M',
                '-.': 'N', '---': 'O', '.--.': 'P',
                '--.-': 'Q', '.-.': 'R', '...': 'S',
                '-': 'T', '..-': 'U', '...-': 'V',
                '.--': 'W', '-..-': 'X', '-.--': 'Y',
                '--..': 'Z', '.----': '1', '..---': '2',
                '...--': '3', '....-': '4', '.....': '5',
                '-....': '6', '--...': '7', '---..': '8',
                '----.': '9', '-----': '0', '--..--': ', ',
                '.-.-.-': '.', '..--..': '?', '-..-.': '/',
                '-....-': '-', '-.--.': '(', '-.--.-': ')'}


# ------------------- FUNCTIONS --------------------------------------------------
def text_to_morse(text):
    morse_code = ''
    for letter in text:
        if letter in MORSE_CODE_DICT.keys():
            morse_code += MORSE_CODE_DICT[letter] + '  '
        elif letter == ' ':
            morse_code += '   '
    pyperclip.copy(morse_code)
    message = 'Morse Code copied to Clipboard!'
    return morse_code + ' \n\n' + message + '\n'


def morse_to_text(morse):
    # First we split it into words by sep of 3 spaces
    morse_inserted = morse.split(sep='   ')

    text = ''
    # We then split each word into letters and then into symbols in each letter
    for word in morse_inserted:
        letters = word.split(sep=' ')
        for symbol in letters:
            if symbol in LETTERS_DICT.keys():
                text += LETTERS_DICT[symbol]
        # We add a space here to separate each words
        text += ' '
    pyperclip.copy(text)
    message = 'Text copied to Clipboard!'
    return text + ' \n\n' + message + '\n'


# --------------------------------------------------------------------
# Title of program
print(title)

translator_on = True
while translator_on:
    print(separator)

    user_choice = input("Insert 'text' if your input is text or 'morse' if your input is Morse code: ")

    if user_choice == 'text':
        user_text = input("Insert text here: ").upper()

        # ------------------ From TEXT to MORSE CODE ----------------------------
        print(text_to_morse(user_text))

        again = input("Something else to translate? (Insert 'yes' or 'no'): ")
        if again == 'yes' or again == 'Yes' or again == 'y':
            continue
        else:
            translator_on = False


    elif user_choice == 'morse':
        print('''
         -- Make sure you leave 
        two (2) spaces between symbols 
        and three(3) spaces between words 
        in Morse code --
        ''')
        user_text = input("Insert your morse code here: ")
        # ------------------ From MORSE CODE to TEXT ----------------------------
        print((morse_to_text(user_text)))

        again = input("Something else to translate? (Insert 'yes' or 'no'): ")
        if again == 'yes' or again == 'Yes' or again == 'y':
            continue
        else:
            translator_on = False

print(separator)
print('\t' * 2, '    Bye bye. Have a great day.')
print(separator)
