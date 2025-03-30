# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 12/31/2024 - 12:02PM 
# Script Purpose : Base64 Encoder/Decoder tool coded in Python
# Description    : This script allows users to:
#                  1. Encode a message into Base64 format.
#                  2. Decode a Base64 encoded message back to its original text.
# 
# Features       : 
#                  - Encode Messages: Convert text messages into Base64 encoded format.
#                  - Decode Messages: Convert Base64 encoded messages back into their original text form.
#                  - Clear Screen: Provides a clean interface by clearing the screen before and after each operation.
#                  - User-Friendly Interface: Keeps running until the user chooses to exit, allowing multiple operations in one session.
#
# Requirements   : 
#                  - Python 3.x installed on your machine.
#
# Usage Note     : Ensure you have Python installed and follow the setup guide for running the script.
# ===================================================================================
import base64
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def encode_base64(message):
    encoded_message = base64.b64encode(message.encode('utf-8'))
    return encoded_message.decode('utf-8')

def decode_base64(encoded_message):
    decoded_message = base64.b64decode(encoded_message.encode('utf-8'))
    return decoded_message.decode('utf-8')

def main():
    while True:
        clear_screen()
        print("Base64 Encoder/Decoder")
        print("Choose an option:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")

        option = input("Enter the number of the option you want to choose: ")

        clear_screen()

        if option == '1':
            message = input("Enter the message to encode: ")
            encoded_message = encode_base64(message)
            print(f'Encoded Message: {encoded_message}')
        elif option == '2':
            encoded_message = input("Enter the message to decode: ")
            decoded_message = decode_base64(encoded_message)
            print(f'Decoded Message: {decoded_message}')
        elif option == '3':
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid number.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
