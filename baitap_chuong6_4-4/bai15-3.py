_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

new = []

for x in _tuple:
    if x not in new:
        new.append(x)

new_tuple = tuple(new)

print(new_tuple)