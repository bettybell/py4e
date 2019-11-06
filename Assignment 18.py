import string

letters = {}
fname = input('Enter file name: ')
fhandle = open(fname)

for line in fhandle:
	words = line.split()
	for word in words:
		for char in word:
			char = char.lower()
			if char.isalpha():
				letters[char] = letters.get(char, 0) + 1
letterlist = []

for letter, count in letters.items():
	letterlist.append( (count, letter) )
letterlist.sort(reverse = True)
print(letterlist)