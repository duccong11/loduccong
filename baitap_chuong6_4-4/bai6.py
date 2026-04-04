lst = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

new = []
for x in lst:
    if x not in new:
        new.append(x)

print(new)