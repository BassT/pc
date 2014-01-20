import sys
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
##original = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
original = 'map'
chars = []
for c in original:
	try:
		index = letters.index(c)
		if index >= (len(letters) - 2):
			c = letters[index - (len(letters) - 2)]
		else:
			c = letters[index + 2]
		chars.append(c)
	except ValueError:
		chars.append(c)
sys.stdout.write(''.join(chars))
sys.stdout.flush()
