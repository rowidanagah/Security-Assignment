from caesar import caesar_decrypt, caesar_encryption
from vigenere import vigenere_decrypt, vigenere_encrypt
from Playfair import playfair_encrypt
import argparse

# python parse.py -alg casear -k=2 -en no -txt=dana
def run(args):
    text, key, alg, enc = args.text, args.key, args.algorithm, args.encryption
    if alg == "casear":
        key = int(key)
        if enc =='yes':
            encryptedText = caesar_encryption(text,key)
            return encryptedText
        else:
            plainText = caesar_decrypt(text,key)
            return plainText
    elif alg == "vigenere":
        if enc == "yes":
            encryptedText = vigenere_encrypt(text,key)
            return encryptedText
        else:
            plainText = vigenere_decrypt(text,key)
            return plainText
    else:
        plainText = playfair_encrypt(text, key)
        return plainText

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-alg", "--algorithm", type= str, required =True,
        choices= ['hill', 'casear', 'outokey', 'playfair', 'vigenere'])
    parser.add_argument('-k', '--key', required= True)
    parser.add_argument("-en", "--encryption", type = str, default ='yes', choices= ["yes" , "no"])
    parser.add_argument("-txt", '--text', type =str)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    txt = run(args)
    print(txt)

