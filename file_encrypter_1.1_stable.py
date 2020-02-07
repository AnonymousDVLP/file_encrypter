from random import sample
from itertools import product as col
import sys, argparse


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
    
    parser = argparse.ArgumentParser(prog=sys.argv[0], usage='%(prog)s [--encrypt/--decrypt] [options]', description="Vigenere cryptography file encrypter - 2020 Lorenzo Antonello")
    # Argomenti
    parser.add_argument("--encrypt", help="Encrypt the file", action="store_true")
    parser.add_argument("--decrypt", help="Decrypt the file", action="store_true")
    parser.add_argument("-k", "--key", help="Key")
    parser.add_argument("-i", "--input", help="Input file name")
    parser.add_argument("-o", "--output", help="Output file name")
    parser.add_argument("-l", "--length", help="Length of the key")
    parser.add_argument("-p", "--keypart", help="Part of the key")
    parser.add_argument("--nokey", help="If you don't remember the key", action="store_true")
    
    args = parser.parse_args()
    
    if args.encrypt == True:
        encrypt = True
        if args.key:
            key = args.key.upper()
        else:
            print("[!] Errore: Dichiarare la chiave con -k.")
            sys.exit()
        if args.output:
            output_file = args.output
        else:
            print("[!] Errore: Dichiarare il file di output con -o.")
            sys.exit()
        try:
            with open(args.input, 'r') as file:
                x = file.read().upper()
        except FileNotFoundError:
            print("[!] Errore: File non trovato, dichiarare il nome del file da criptare.")
            sys.exit()
        except TypeError:
            print("[!] Errore: Dichiarare il file di input con -i.")
            sys.exit()
        print("[*] Criptazione in corso...")
        output = vigenere(x,key)
        z = open(output_file, "w")
        z.write(output)
        z.close()
        print(f"[*] File criptato con successo in: {output_file}")
        sys.exit()
    
    elif args.decrypt == True:
        encrypt = False
        if args.nokey == True:
            abc = list("ABCDEFGHIJKHIJKLMNOPQRSTUVWXYZ")
            if args.length:
                length = args.length
                try:
                    with open(args.input, 'r') as file:
                        x = file.read().upper()
                except FileNotFoundError:
                    print("[!] Errore: File non trovato, dichiarare il nome del file da decriptare.")
                    sys.exit()
                except TypeError:
                    print("[!] Errore: Dichiarare il file di input con -i.")
                    sys.exit()
                while True:
                    key_gen = ''.join(sample(abc,length))
                    print(f"for {key_gen} = {vigenere(x,key_gen)}")
                    if input('continue(y/n) ... : ')== "n":
                        sys.exit()
            else:
                if args.keypart:
                    key = args.keypart
                    try:
                        with open(args.input, 'r') as file:
                            x = file.read().upper()
                    except FileNotFoundError:
                        print("[!] Errore: File non trovato, dichiarare il nome del file da decriptare.")
                        sys.exit()
                    except TypeError:
                        print("[!] Errore: Dichiarare il file di input con -i.")
                        sys.exit()
                    list_of_keys = generator(key,'?',len(key))
                    for k in list_of_keys:
                        print(f'for {k} ==> {vigenere(x,k)}')
                else:
                    print("[!] Errore: Dichiarare -l o -p.")
                    sys.exit()
        else:
            if args.key:
                key = args.key.upper()
            else:
                print("[!] Errore: Dichiarare la chiave con -k o usare --nokey.")
                sys.exit()
            if args.output:
                output_file = args.output
            else:
                print("[!] Errore: Dichiarare il file di output con -o.")
                sys.exit()
            try:
                with open(args.input, 'r') as file:
                    x = file.read().upper()
            except FileNotFoundError:
                print("[!] Errore: File non trovato, dichiarare il nome del file da decriptare.")
                sys.exit()
            except TypeError:
                print("[!] Errore: Dichiarare il file di input con -i.")
                sys.exit()
            print("[*] Decriptazione in corso...")
            output = vigenere(x,key)
            z = open(output_file, "w")
            z.write(output)
            z.close()
            print(f"[*] File decriptato con successo in: {output_file}")
            sys.exit()
    else:
        try:
            sys.argv[1]
        except:
            parser.print_help()