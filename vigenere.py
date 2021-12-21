def vigenere_encrypt(plaintext, key):
    """
    1 - clac ord of each ch if both plaintext and the key
    2 - clac len of both of them
    3 - adding % 26, and to fex len of the key :: loop over the plaintext len % key len

    """
    ord_plaintext, ord_key = [ord(i) for i in plaintext], [ord(i) for i in key] 
    encrypted_text, len_of_txt, len_of_key = '', len(plaintext), len(key)
    for i in range(len_of_txt):
        val =  (ord_plaintext[i] + ord_key[i% len_of_key]) % 26
        if plaintext[i].isupper():
            encrypted_text += chr(val+65)
        else:
            encrypted_text += chr(val+97)
    return encrypted_text


def vigenere_decrypt(plaintext, key):
    """
    1 - clac ord of each ch if both plaintext and the key
    2 - clac len of both of them
    3 - adding % 26, and to fex len of the key :: loop over the plaintext len % key len

    """
    ord_plaintext, ord_key = [ord(i) for i in plaintext], [ord(i) for i in key] 
    encrypted_text, len_of_txt, len_of_key = '', len(plaintext), len(key)
    for i in range(len_of_txt):
        val =  (ord_plaintext[i] - ord_key[i% len_of_key]) % 26
        if plaintext[i].isupper():
            encrypted_text += chr(val+65)
        else:
            encrypted_text += chr(val+97)
    return encrypted_text
"""
print(encrypt("CODESPEEDY" , 'TIME'))
print(decrypt("VWPILXQIWG" , 'TIME'))
VWPILXQIWG
"""