def convertPlainTextToDiagraphs(plainText):
	"""
	Split the plaintext itno 2 unique qairs
	"""
	n, tmp = len(plainText), 0
	for i in range(0,n+1,2):
		if i < n-1:
			if plainText[i] == plainText[i+1]:
				plainText=plainText[:i+1]+'X'+plainText[i+1:]
				tmp += 1 # to keep track of the inserted chr
	if n+tmp % 2:
		plainText += 'x'
	return plainText

def generateKeyMatrix(key):

	"""
	Function to generate a cipher key matrix
	"""
	matrix, filter_key = [[' ' for i in range(5)]for j in range(5)], []
	"""
	1- Remove Duplications in the key
	2- Substitute J occerance with I
	"""
	for ch in key:
		if ch not in filter_key:
			if ch == 'j':
				filter_key.append('i')
			else:			
				filter_key.append(ch)
	iflagg = 'i' in filter_key
	"""
     Fill the remaining SimpleKeyArray with rest of unused letters from english alphabets 
	"""
	alpha = 'abcdefghiklmnopqrstuvwxyz'
	for ch in alpha:
		if ch not in filter_key:
			filter_key.append(ch)
			
	"""
		Mapping the filter_key to a 5*5 matrix
	"""
	for i in range(5):
		for j in range(5):
			matrix[i][j] = filter_key[(i*5)+j]
	return matrix

def indexLocator(ch , matrix):
	if ch == 'j':
		ch = 'i'
	for i,x in enumerate(matrix):
		for j,y in enumerate(x):
			if ch == y :
				return i,j

def playfair_encrypt(plainText, key):
	encrypted_text = []
	matrix = generateKeyMatrix(key)
	massege = convertPlainTextToDiagraphs(plainText)
	n = len(massege)
	
	for ch in range(0,n-1,2):
		row1, col1 =  indexLocator(massege[ch],matrix)
		row2, col2 =  indexLocator(massege[ch+1],matrix)
		
		"""
		# if same column then look in below row so
        # now to see below row => increase the row in both item take the mod 
        # (row1[0]+1,col1[1]) => ((3+1)%5,1) => (4,1)
        # (row2[0]+1,col2[1]) => ((4+1)%5,1) => (5,1)
        
		# if same row then
        # now to see col above => increase the row in both item take the mod 
        # (row1[0]+1,col1[1]) => ((3+1)%5,1) => (4,1)
        # (row2[0]+1,col2[1]) => ((4+1)%5,1) => (5,1)
		

		# diff cols nor diff rows
		# swap cols of both vals
		"""
		
		if row2 == row1 :
			col1 = (col1+1) % 5
			col2 = (col2+1) % 5
			encrypted_text.append(matrix[row1][col1])
			encrypted_text.append(matrix[row2][col2])

		elif col2 == col1 :
			row1 = (row1+1) % 5
			row2= (row2+1) % 5
			encrypted_text.append(matrix[row1][col1])
			encrypted_text.append(matrix[row2][col2])
		else :
			encrypted_text.append(matrix[row1][col2])
			encrypted_text.append(matrix[row2][col1])
	return ''.join(encrypted_text)     

"""
plainText = "instruments"

key = "Monarchy".lower()
msg = convertPlainTextToDiagraphs(plainText)
enc = "".join(encrypt(msg,key))
print(enc)
"""