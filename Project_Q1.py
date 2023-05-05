# Load Dictionary
def load_dictionary(MORSE_CODE_DICT):
    
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...','C':'-.-.', 
                        'D':'-..', 'E':'.','F':'..-.', 
                        'G':'--.', 'H':'....','I':'..', 
                        'J':'.---', 'K':'-.-','L':'.-..', 
                        'M':'--', 'N':'-.','O':'---', 
                        'P':'.--.', 'Q':'--.-','R':'.-.', 
                        'S':'...', 'T':'-', 'U':'..-', 
                        'V':'...-', 'W':'.--', 'X':'-..-', 
                        'Y':'-.--', 'Z':'--..', '1':'.----', 
                        '2':'..---', '3':'...--', '4':'....-', 
                        '5':'.....', '6':'-....', '7':'--...', 
                        '8':'---..', '9':'----.','0':'-----', 
                        ', ':'--..--', '.':'.-.-.-','?':'..--..', 
                        '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}
    return MORSE_CODE_DICT

# Function to encrypt the string according to the morse code chart
def encrypt(message, MORSE_CODE_DICT):
        cipher = ''
        for letter in message:
                if letter != ' ':

                        # Looks up the dictionary and adds the
                        # correspponding morse code
                        # along with a space to separate
                        # morse codes for different characters
                        cipher += MORSE_CODE_DICT[letter] + ' '
                else:
                        # 1 space indicates different characters
                        # and 2 indicates different words
                        cipher += ' '

        return cipher

# Function to decrypt the string from morse to english
def decrypt(message, MORSE_CODE_DICT):

        # extra space added at the end to access the
        # last morse code
        message += ' '

        decipher = ''
        citext = ''
        for letter in message:

                # checks for space
                if (letter != ' '):

                        # counter to keep track of space
                        i = 0

                        # storing morse code of a single character
                        citext += letter

                # in case of space
                else:
                        # if i = 1 that indicates a new character
                        i += 1

                        # if i = 2 that indicates a new word
                        if i == 2 :

                                # adding space to separate words
                                decipher += ' '
                        else:

                                # accessing the keys using their values (reverse of encryption)
                                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                .values()).index(citext)]
                                citext = ''

        return decipher

def print_menu():
    
    print("Hello, this program allows you to translate text to morse code or translate morse code to text")
    print()
    print("Please, select one of the below options:")
    print()
    print("*** enter 't' for encoding text")
    print("*** enter 'm' for decoding morse code")
    print("*** enter 'e' to exit the program.")
    
    choice = input("\nMy input is: ")
    
    while True:
        if choice == 't' or choice == 'm' or choice == 'e':
            return choice
        else:
            print("***invalid option***")
            choice = input("Please enter a valid option: ")
    
# Hard-coded driver function to run the program
def main():
    
    # Dictionary representing the morse code chart
    MORSE_CODE_DICT = {}

    MORSE_CODE_DICT = load_dictionary(MORSE_CODE_DICT)
    
    while True:
        choice = print_menu()
        
        if choice == 't':
            text = input("\nPlease enter text to translate:\n")
            morse = encrypt(text.upper(), MORSE_CODE_DICT)
            print (morse)
            print()
        
        elif choice == 'm':
            morse = input("\nPlease enter morse to translate:\n")
            text = decrypt(morse.upper(), MORSE_CODE_DICT)
            print (text)
            print()
            
        else:
            print("\nThanks for using this program.\n")
            break

# Executes the main function
main()
