
import itertools

abbrs = []
with open('elements','r') as file:
    lines = file.readlines()
    for line in lines:
        x = line.split('-')
        abbrs.append(x[1].strip())

print(abbrs)
check_list = []
output = []
found_list = []
text = input('Enter word: ')
text = text.lower()
# with open('2of12.txt') as file:
#   lines = file.readlines()

#   for line in lines:
#       text = line.strip()
#check_list[:] = []
for x in range(len(text)):
    for y in range(3):
        check_list.append(text[x:x + y + 1])

print(check_list)
#found_list[:] = []
for item in abbrs:
    if item.lower() in check_list:
        found_list.append(item)

print([text, sorted(found_list)])

search = {}
for letter in text:
    search_list = []
    for item in found_list:
        if letter == item[0].lower():
            search_list.append(item)
    search[letter] = search_list

print(search)

output = text.split()


# for key in search:
#   if search[key] == []:
#       print('word not possible')
#       quit()

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        print(node)
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

print(find_path(output, text[0], text[-1]))

