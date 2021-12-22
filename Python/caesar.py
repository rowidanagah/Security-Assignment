def caesar_encryption(plaintext,key):
	encrypted_text = ''
	for ch in plaintext:
		# Encrypt Upper char
		if ch.isupper():
			tmp = chr(65 + ((ord(ch) - 65 + key) % 26))
		# Encrypt lowercase char
		else :
			tmp = chr(97 + ((ord(ch) - 97 + key) % 26))
		encrypted_text +=  tmp
	return encrypted_text


def caesar_decrypt(encrypted_text,key):
	plaintext = ''
	for ch in encrypted_text:
		if not ch:
			plaintext += ''
		elif ch.isupper():
			plaintext += chr((ord(ch) - key - 65) % 26 + 65)
		else :
			plaintext += chr((ord(ch) - key - 97) % 26 + 97)
	return plaintext

"""
print(caesar_encryption("ahmed" , 5))
print(caesar_decrypt("fmrji" , 5))

"""