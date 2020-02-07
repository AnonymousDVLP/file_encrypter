from random import sample
from itertools import product as col
import os, sys

def generator(key,char,length):
    char_len = key.count(char)   
    key_piece = key[:length - char_len:]
    list_keys = [key_piece+"".join(i) for i in list(col([chr(i) for i in range(65, 65+26)], repeat=char_len))]
    return list_keys
	
def vigenere(x,key):
    lst_final = []
    code = list(x)
    j = 0
	
    for i,char in enumerate(code):
        if char.isalpha():
            code[i] = key[(i+j)%len(key)]
            if encrypt:
                lst_final.append((ord(x[i]) + ord(code[i]) - 65 * 2) % 26)
            else:
                lst_final.append((ord(x[i]) - ord(code[i])) % 26)
        else:
            lst_final.append(ord(char))
            j -=1

    for i,char in enumerate(code):
        if char.isalpha():
            lst_final[i] = chr(lst_final[i] + 65)
        else:
            lst_final[i] = chr(lst_final[i])
			
    return ''.join(lst_final)

if __name__ == "__main__":
    pr_name = sys.argv[0]
    try:
	    sys.argv[1]
    except:
	    print(f'''

FILE ENCRYPTER beta 0.1.0 - 2020 Lorenzo Antonello
Vigenere encryption

usage: python3 {pr_name} <options> <filename>

Examples:

    python3 {pr_name} encrypt -k thisisthekey -o encrypted_file.txt file.txt
    python3 {pr_name} decrypt -k thisismykey -o decrypted_file.txt file.txt
    python3 {pr_name} decrypt --nokey -p thisis????? file.txt

Options:

    -h, --help       : Displays this usage screen
    encrypt          : Encrypt the file
    decrypt          : Decrypt the file
    -k, --key        : Key (Encr/Decr)
    --nokey          : If you don't remember the key (Decryption)
    -l, --length     : Length of the key (Decryption)
    -p, --keypart    : Part of the key that you remember(Decryption)
    -o, --output     : Output file name (Encr/Decr)\n''')

    else:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            os.system(f"python3 {pr_name}")
            sys.exit()
        elif sys.argv[1] == "encrypt":
            encrypt = True
            if sys.argv[2] == "-k" or sys.argv[2] == "--key":
                key = sys.argv[3].upper()
                if sys.argv[4] == "-o" or sys.argv[4] == "--output":
                    output_file = sys.argv[5]
            elif sys.argv[2] == "-o" or sys.argv[2] == "--output":
                output_file = sys.argv[3]
                if sys.argv[4] == "-k" or sys.argv[4] == "--key":
                    key = sys.argv[5].upper()
            with open(sys.argv[6], 'r') as file:
                x = file.read().upper()
            output = vigenere(x,key)
            z = open(output_file, "w")
            z.write(output)
            z.close()
            sys.exit()
        elif sys.argv[1] == "decrypt":
            encrypt = False
            if sys.argv[2] == "-k" or sys.argv[2] == "--key":
                key = sys.argv[3].upper()
                if sys.argv[4] == "-o" or sys.argv[4] == "--output":
                    output_file = sys.argv[5]
                with open(sys.argv[6], 'r') as file:
                    x = file.read().upper()
                output = vigenere(x,key)
                z = open(output_file, "w")
                z.write(output)
                z.close()
                sys.exit()
            elif sys.argv[2] == "-o" or sys.argv[2] == "--output":
                output_file = sys.argv[3]
                if sys.argv[4] == "-k" or sys.argv[4] == "--key":
                    key = sys.argv[5].upper()
                with open(sys.argv[6], 'r') as file:
                    x = file.read().upper()
                output = vigenere(x,key)
                z = open(output_file, "w")
                z.write(output)
                z.close()
                sys.exit()
            
            elif sys.argv[2] == "--nokey":
                abc = list("ABCDEFGHIJKHIJKLMNOPQRSTUVWXYZ")
                if sys.argv[3] == "-l" or sys.argv[3] == "--length":
                    length = sys.argv[4]
                    with open(sys.argv[5], 'r') as file:
                        x = file.read().upper()
                    while True:
                        key_gen = ''.join(sample(abc,length))
                        print(f"for {key_gen} = {vigenere(x,key_gen)}")
                        if input('continue(y/n) ... : ')== "n":
                            break
                elif sys.argv[3] == "-p" or sys.argv[3] == "--keypart":
                    key = sys.argv[4]
                    with open(sys.argv[5], 'r') as file:
                        x = file.read().upper()
                    list_of_keys = generator(key,'?',len(key))
                    for k in list_of_keys:
                        print(f'for {k} ==> {vigenere(x,k)}')
