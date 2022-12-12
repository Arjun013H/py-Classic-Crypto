from tabulate import tabulate
import string
import secrets


def logo():
    a = '''

    ___________________ _________  
    \______   \_   ___ \\_   ___ \ 
    |     ___/    \  \//    \  \/ 
    |    |   \     \___\     \____
    |____|    \______  /\______  /
                    \/        \/ 

    '''
    print(a)


def substitution_cipher():
    cipher_txt = ""
    plain_txt = ""
    all_letters = string.ascii_letters

    def enc_dec_msg(key, message, mode):
        translated = ''
        charA = all_letters
        charB = key
        if mode in ("Decrypt", "decrypt", "D", "d"):
            # print("hi")
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

    def checkValidKey(key):
        key_list = list(key)
        letters_list = list(string.ascii_letters)
        key_list.sort()
        letters_list.sort()
        if key_list != letters_list:
            print("Not A Valid Key ")
            return False
        return True

    def brute():
        pass
    mode = input("Encrypt/Decrypt/Brute (E/D/Brute) ")
    if mode in ("Decrypt", "decrypt", "D", "d"):
        message = input("Enter CT:")
        key = input("Enter key:")
    elif mode in ("encrypt", "E", "e"):
        message = input("Enter PT:")
        key = input("Enter key:")
        if key == "":
            key = gen_Key()
            print(f"the key is {key}")
    elif mode in ("Brute", "B", "b"):
        message = input("Enter CT:")
        mode = 'brute'

    if mode == 'brute':

        return

    if checkValidKey(key) == False:
        return
    msg = enc_dec_msg(key, message, mode)

    print(f"the transalated message is \n{msg}")


def Caesar_Cipher():
    # Caesar Cipher

    mode = input("Decrypt/Encrypt/Brute (D/E/B) ")
    if mode in ("Decrypt", "decrypt", "D", "d"):
        message = input("Enter CT:")
        key = int(input("Enter key:"))
        mode = 'decrypt'
    elif mode in ("encrypt", "E", "e"):
        message = input("Enter PT:")
        key = input("Enter key:")
        if key == '':

            key = secrets.SystemRandom(1).randint(1, 25)
        key = int(key) % 26
        if key == 0:
            print("Not a Vaid Key")
            return
        print(f"the key is {key}")
        mode = 'encrypt'
    elif mode in ("Brute", "B", "b"):
        message = input("Enter CT:")
        mode = 'brute'

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    translated = ''

    if mode == 'brute':

        for key in range(len(LETTERS)):

            translated = ""

            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key

                    if num < 0:
                        num = num + len(LETTERS)

                    translated = translated + LETTERS[num]

                else:
                    translated = translated + symbol

            print("Key #%s: %s" % (key, translated))
        return

    # message = message.upper()

    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num = LETTERS.find(symbol)  # get the number of the symbol
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
    print(f'the {mode}ed text is {translated}')
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

    logo()
    while True:

        l = [[1, "substitution cipher"], [2, "The Caesar Cipher"], [10, "exit"]]
        table = tabulate(l, headers=['slno', 'Cipher'], tablefmt='pretty')
        print(table)
        main()
