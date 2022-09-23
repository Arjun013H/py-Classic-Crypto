from tabulate import tabulate
import string
import secrets


def substitution_cipher():
    cipher_txt = ""
    plain_txt = ""
    all_letters = string.ascii_letters

    def enc_dec_msg(key, message, mode):
        translated = ''
        charA = all_letters
        charB = key
        if mode in ("Decrypt", "decrypt", "D", "d"):
            print("hi")
            charA, charB = charB, charA

        for symbol in message:
            indexid = charA.find(symbol)
            if indexid == -1:
                translated = translated + symbol
            else:
                translated = translated + charB[indexid]

        return translated

    def gen_Key():
        key = list(all_letters)
        secrets.SystemRandom(1).shuffle(key)
        return "".join(key)

    mode = input("Decrypt/Encrypt (D/E) ")
    if mode in ("Decrypt", "decrypt", "D", "d"):
        message = input("Enter CT:")
        key = input("Enter key:")
    elif mode in ("encrypt", "E", "e"):
        message = input("Enter PT:")
        key = gen_Key()
        print(f"the key is {key}")
    msg = enc_dec_msg(key, message, mode)

    print(f"the transalated message is \n{msg}")

def Caesar_Cipher():
    # Caesar Cipher

    mode = input("Decrypt/Encrypt (D/E) ")
    if mode in ("Decrypt", "decrypt", "D", "d"):
        message = input("Enter CT:")
        key = int(input("Enter key:"))
        mode = 'decrypt'
    elif mode in ("encrypt", "E", "e"):
        message = input("Enter PT:")
        key = secrets.SystemRandom(1).randint(1,25)
        print(f"the key is {key}")
        mode = 'encrypt'

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    message = message.upper()
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num = LETTERS.find(symbol) # get the number of the symbol
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol
    # print the encrypted/decrypted string to the screen
    print(translated)
    # copy the encrypted/decrypted string to the clipboard



def main():

    slno_input = int(input("Enter menu Number:-"))

    if slno_input == 1:
        substitution_cipher()
    elif slno_input == 2:
        Caesar_Cipher()
    elif slno_input == 10:
        exit()
    else:
        print("enter a valid menu number!!")
        main()


if __name__ == '__main__':
    while True:

        l = [[1, "substitution cipher"],[2,"The Caesar Cipher"], [10, "exit"]]
        table = tabulate(l, headers=['slno', 'Cipher'], tablefmt='pretty')
        print(table)
        main()

