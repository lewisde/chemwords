class Node:
  def __init__(self, value):
    self.value = value
    self.children = []
    self.complete = False

elemset = {'mn', 'h', 'sc', 'li', 'po', 'i', 'hf', 'ar', 'sr', 'al', 'ir', 'br', 'mg', 'tm', 'db', 'ce', 'bi', 'he', 'fm', 'nd', 'n', 'cd', 'no', 'cf', 'c', 'ds', 'cr', 'rf', 'cu', 'mt', 'gd', 'p', 'fl', 'cs', 'pt', 'eu', 'md', 'be', 'lu', 's', 'pa', 'xe', 'pb', 'ra', 'co', 'b', 'k', 'zn', 'os', 'te', 'ca', 'cn', 'pd', 'ag', 'ni', 'bk', 'se', 'sb', 'as', 'rn', 'pm', 'yb', 'v', 'kr', 'lr', 'o', 'ge', 'tl', 'fr', 'sm', 'uuo', 'np', 'ru', 'na', 'f', 'uup', 'uus', 're', 'dy', 'rb', 'ne', 'hs', 'cm', 'ta', 'at', 'mo', 'th', 'au', 'pu', 'u', 'zr', 'rh', 'ac', 'es', 'y', 'sg', 'ho', 'in', 'cl', 'pr', 'ti', 'si', 'la', 'lv', 'sn', 'w', 'bh', 'fe', 'rg', 'tc', 'ba', 'uut', 'er', 'ga', 'hg', 'tb', 'am', 'nb'}

# let's assume this is filled with the elements (lowercased)
word = input('enter a word: ')
root = Node(None)
 
def build_tree(node, word):
  if not word:
    node.complete = True
    return
  
  if word[0].lower() in elemset:
    child = Node(word[0])
    node.children.append(child)
    build_tree(child, word[1:])
  if len(word) > 1 and word[:2].lower() in elemset:
    child = Node(word[:2])
    node.children.append(child)
    build_tree(child, word[2:])
 
build_tree(root, word)

word_list = []
def print_words(node, word=''):
    global word_list 
    if node.value:
        word += node.value.title()
    if node.complete:
        word_list.append(word)
    for child in node.children:
        print_words(child, word)


print_words(root)

print(word_list)

 
# now your tree should contain all the words
# nodes marked complete should represent finsihed words
