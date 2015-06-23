def find_element_word(text):
	words = []
	with open('chemwords.txt') as file:
		words = file.readlines()
	for row in words:
		x = row.strip()
		if text.lower() == x.lower():
			return x
	else:
		return 'not possible'

prompt = input('Enter a word to check: ')
while prompt != 'quit':
	print(find_element_word(prompt))
	prompt = input('Enter a word to check: ')