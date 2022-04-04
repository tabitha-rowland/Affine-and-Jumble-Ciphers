from audioop import mul
import random
import string
import math

#affine cipher project
#This project will provide the user with 5 options, print encoding tables, encode message, 
#decode message, change the shift by value, and quit. The message that the user encodes will 
# be done using a randomly selected value for a that fits within the necessary parameters. 

#check_a param: alphabet size. Checks if a is valid, needs comparable int. 
#create_shift_substitutions param: n (which is shift amount) and a (which is multiplication amount)


#Author: Tabitha Rowland
#With some help from: Erin Murphy



def check_a(alphabet_size): #ensures that the gcd of a and the alphabet size is only 1
    a = random.randint(0, 25) #generate random number for a
    while math.gcd(a, alphabet_size) != 1: 
        a = random.randint(0, 25) #if gcd not 1 then reselect a
        print(a) 
    return a # return a if the gcd is 1





def create_shift_substitutions(n, a):
    print(f"a: {a}, n: {n}.")
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter  = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i*a+n)%alphabet_size] #only change from textbook code, i*a

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
    n = 1 #if no input, assume shift is 1
    a = check_a(26) #find valid a value
    encoding, decoding = create_shift_substitutions(n, a)
    while True: 
        print("\nAffine Encoder Decoder ")
        print("---------------------- ")
        print("\tCurrent Shift: {}\n".format(n))
        print("\tCurrent Multiplication: {}\n".format(a))
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message.")
        print("\t3. Decode Message.")
        print("\t4. Change Shift.")
        print("\t5. Quit.\n")
        choice = input(">> ")
        print()

        if choice == '1':
            print("Encoding Table:")
            print(printable_substitution(encoding))
            print("Decoding Table:")
            print(printable_substitution(decoding))

        elif choice == '2':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(encode(message.upper(), encoding)))

        elif choice == '3':
            message = input("\nMessage to decode: ")
            print("Decoded Message: {}".format(decode(message.upper(), decoding)))

        elif choice == '4':
            new_shift = input("\nNew Shift (currently {}): ".format(n))
            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    raise Exception("Shift must be greater than 0")
            except ValueError:
                print("Shift {} is not a valid number.".format(new_shift))
            else:
                n = new_shift
                a = check_a(26)
                encoding, decoding = create_shift_substitutions(n, a)
        
        elif choice == '5':
            print("Goodbye! \n")
            break

        else:
            print("unknown option {}.".format(choice))

