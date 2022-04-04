from audioop import mul
import random
import string
import math

#jumble cipher project
#This project will provide the user with 4 options, print encoding tables, encode message, 
#decode message, and quit. The message that the user encodes will be done using a randomly 
# ordered alphabet.

#Author: Tabitha Rowland
#With some help from: Erin Murphy



def create_jumble_substitutions():
    encoding = {}
    decoding = {}

    alphabet_size = len(string.ascii_uppercase)
    alphabet = list(string.ascii_uppercase) #make an alphabet list and then shuffle it
    random.shuffle(alphabet)



    for i in range(alphabet_size):
        letter  = string.ascii_uppercase[i]
        subst_letter = alphabet[i]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding


def encode(message,subst):
    cipher = ""
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher

def decode(message, subst):
        return encode(message, subst)


def printable_substitution(subst):
    mapping = sorted(subst.items())

    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(subst_letter for _, subst_letter in mapping)
    return "{}\n{}".format(alphabet_line, cipher_line)


if __name__ == "__main__":
    encoding, decoding = create_jumble_substitutions()
    while True: 
        print("\nJumble Encoder Decoder ")
        print("---------------------- ")
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message.")
        print("\t3. Decode Message.")
        print("\t4. Quit.\n")
        choice = input(">> ")
        print()

        if choice == '1':
            print("Encoding Table:")
            print(printable_substitution(encoding))
            print("Decoding Table:")
            print(printable_substitution(decoding))

        if choice == '2':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(encode(message.upper(), encoding)))

        elif choice == '3':
            message = input("\nMessage to decode: ")
            print("Decoded Message: {}".format(decode(message.upper(), decoding)))

        elif choice == '4':
            print("Goodbye! \n")
            break

        else:
            print("unknown option {}.".format(choice))

