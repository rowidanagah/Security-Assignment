from Python.caesar import caesar_decrypt, caesar_encryption
from Python.vigenere import vigenere_decrypt, vigenere_encrypt
from Python.Playfair import playfair_encrypt
import argparse

def run(args):
    text, key, alg, enc = args.text, args.key, args.algorithm, args.encryption
    print("Text is " , text, "\nKey is ", key, "\nAlgorith Used ", alg, "\nEncryption ?", enc =="yes" )
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
    text = run(args)
    print("   ",text)