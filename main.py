import pyperclip, sys, random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

 
def sub_main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of m  yths is explained in this way. -Bert  r and Russell'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
    sub_checkValidKey(myKey)



    if myMode == 'encrypt':
        translated = sub_encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = sub_decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))

    print('The %sed message is:' % (myMode))

    print(translated)

    pyperclip.copy(translated)

    print()

    print('This message has been copied to the clipboard.')





def sub_checkValidKey(key):

    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:

        sys.exit('There is an error in the key or symbol set.')





def sub_encryptMessage(key, message):

    return sub_translateMessage(key, message, 'encrypt')



def sub_decryptMessage(key, message):
    return sub_translateMessage(key, message, 'decrypt')
def sub_translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA,charsB = charsB,charsA


    # loop through each symbol in the message

    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()

            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
            return translated




def sub_getRandomKey():

    key = list(LETTERS)

    random.shuffle(key)

    return ''.join(key)


if __name__ == '__main__':

    sub_main();
