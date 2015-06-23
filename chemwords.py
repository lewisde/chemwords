class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.complete = False

elemset = {'mn', 'h', 'sc', 'li', 'po', 'i', 'hf', 'ar', 'sr', 'al', 'ir', 'br', 'mg', 'tm', 'db', 'ce', 'bi', 'he', 'fm', 'nd', 'n', 'cd', 'no', 'cf', 'c', 'ds', 'cr', 'rf', 'cu', 'mt', 'gd', 'p', 'fl', 'cs', 'pt', 'eu', 'md', 'be', 'lu', 's', 'pa', 'xe', 'pb', 'ra', 'co', 'b', 'k', 'zn', 'os', 'te', 'ca', 'cn', 'pd', 'ag', 'ni', 'bk', 'se', 'sb', 'as', 'rn', 'pm', 'yb', 'v', 'kr', 'lr', 'o', 'ge', 'tl', 'fr', 'sm', 'uuo', 'np', 'ru', 'na', 'f', 'uup', 'uus', 're', 'dy', 'rb', 'ne', 'hs', 'cm', 'ta', 'at', 'mo', 'th', 'au', 'pu', 'u', 'zr', 'rh', 'ac', 'es', 'y', 'sg', 'ho', 'in', 'cl', 'pr', 'ti', 'si', 'la', 'lv', 'sn', 'w', 'bh', 'fe', 'rg', 'tc', 'ba', 'uut', 'er', 'ga', 'hg', 'tb', 'am', 'nb'}

# let's assume this is filled with the elements (lowercased)
#word = input('enter a word: ')
solutions = []
root = Node(None)

def build_tree(node, word, solution=''):
    if not word:
        solutions.append(solution)
        node.complete = True
        return

    if word[0].lower() in elemset:
        child = Node(word[0])
        node.children.append(child)
        build_tree(child, word[1:], solution + word[0].title())
    if len(word) > 1 and word[:2].lower() in elemset:
        child = Node(word[:2])
        node.children.append(child)
        build_tree(child, word[2:], solution + word[:2].title())

#build_tree(root, word)

#print(solutions)
with open('2of12.txt', 'r') as file:
    line = file.readline()
    while line:
        word = line.strip()
        build_tree(Node(None), word)
        line = file.readline()
        print(len(solutions))

with open('results.txt', 'w') as file:
    for row in solutions:
        file.write('{}\n'.format(row))


