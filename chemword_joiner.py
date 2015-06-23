words = set()

with open('chemwords.txt', 'r') as file:
	line = file.readline()
	while line:
		line = line.strip()
		words.add(line)
		line = file.readline()
z = len(words)
print(z)
with open('results.txt', 'r') as file:
	line = file.readline()
	while line:
		line = line.strip()
		words.add(line)
		line = file.readline()
print(len(words) - z)

results = list()
for item in words:
	results.append(item)

print(len(results))

with open('new_chemwords.txt', 'w') as file:
	for item in sorted(results):
		file.write('{}\n'.format(item))