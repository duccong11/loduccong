_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

new = []

for x in _tuple:
    if _tuple.count(x) == 1:
        new.append(x)

new_tuple = tuple(new)

print(new_tuple)