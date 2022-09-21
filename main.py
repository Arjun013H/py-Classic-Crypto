
from cgi import print_environ_usage
from email import message
from math import e
from tabulate import tabulate
import string
import secrets


def substitution_cipher():
    cipher_txt=""
    plain_txt=""
    all_letters=string.ascii_letters
    
    def enc_dec_msg(key,message,mode):
        translated=''
        charA= all_letters
        charB= key
        if mode in ("Decrypt","decrypt","D","d"):
            print("hi")
            charA,charB = charB,charA
        
        for symbol in message:
            indexid= charA.find(symbol)    
            

            
        return translated
    def gen_Key():
        key=list(all_letters)
        secrets.SystemRandom(1).shuffle(key)
        return "".join(key)

    mode = input("Decrypt/Encrypt (D/E) ")
    if mode in ("Decrypt","decrypt","D","d"):
        message= input("Enter CT:")
        key = input("Enter key:")
    elif mode in ("encrypt","E","e"):
        message= input("Enter PT:")
        key = gen_Key()
        print(f"the key is {key}")
    msg = enc_dec_msg(key,message,mode)

    print(f"the transalated message is \n{msg}")



int()
def main():
    
    slno_input = int(input("Enter menu Number:-"))

    if slno_input == 1:
        substitution_cipher()
    elif slno_input == 2:
        exit()
    else:
        print("enter a valid menu number!!")
        main()
        

if __name__ == '__main__':
    l=[[1,"substitution cipher"],[2,"exit"]]
    table = tabulate(l, headers=['slno', 'Cipher'], tablefmt='pretty')
    print(table)
    main()