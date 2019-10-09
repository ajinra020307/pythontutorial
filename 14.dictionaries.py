d={
    'name':'ajin',
    'age':21
}

print(d['name'])

for key in d:
    print(key)

for value in d.values():
    print(value)

for key,value in d.items():
    print(key)
    print(value)

d.pop('age')
print(d)