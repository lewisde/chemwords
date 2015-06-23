element_set = {'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', \
    'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', \
    'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', \
    'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', \
    'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', \
    'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', \
    'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', \
    'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', \
    'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', \
    'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', \
    'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', \
    'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', \
    'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', \
    'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Uut', 'Fl', 'Uup', \
    'Lv', 'Uus', 'Uuo'}

word = input('Enter a word: ')
word = word.upper()
result = []

for x in range(len(word)):
    if result == word[:len(result)+1]:
        continue
    if word[x] in element_set:
        result.append(word[x])
    else:
        print('{} not found'.format(word[x]))
        if x+2 < len(word):
            element = word[x:x+2]
            element = '{}{}'.format(element[0],element[1].lower())
            if element in element_set:
                result.append(element)
            else:
                print('{} not found'.format(element))
                if x+3 < len(word):
                    element = word[x:x+3]
                    element = '{}{}{}'.format(element[0],element[1].lower(),element[2].lower())
                    if element in element_set:
                        result.append(element)
                    else:
                        print('{} not found'.format(element))

    print(result)

