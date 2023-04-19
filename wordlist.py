import sys
import itertools
chr =(input("Enter string = "))
print(' ')
n =int(input("Enter string lenth = "))
print(' ')

c =(input("where to save the file = "))
print (" ")
print ("your file is being ready")

for xs in itertools.product(chr, repeat=n):
	file_path = c
	sys.stdout =open(file_path, 'a')
	print (''.join(xs))


