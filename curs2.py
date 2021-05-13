print('Acesta este cursul 2')

name = 'Ana'
if name:
    print(name)
    print(type(name))
else:
    print('Not defined')  # hello

first_person = {'Name': 'John'}
second_person = {'Name': 'John'}

if first_person is second_person:
    print("same location")
else:
    print("not pointing same location")

if first_person == second_person:
    print("same")
else:
    print("not same")

my_str = r'Owners\'s \n\tmanual'
print(my_str)

print(""" jajjajaa
ajajajja
jcdsksa""")

msg = "{name} has {age} years".format(name='Ion', age=18)
print(msg)
msg = "{1} has {0} years".format('Ion', 18)

name = 'Ion'
age = 18
msg = "{name} has {age} years".format(name=name, age=age)
msg2 = f"{name} has {age + 2} years"
print(msg)
print(msg2)

my_list = [1, 2, 3, 'Ana are mere', True, False, None, [4, 5, 6]]
print(my_list[2])

my_list[2] = 99
print(my_list[2])

inventar = ['faina', 'drojdie', 'apa', 'sare']

for item in inventar:
    print(item)

for index,value in enumerate(inventar):
    print(f"{value} cu index {index}")

print(inventar[-1])
max = len(inventar)
print(inventar[len(inventar) - 1])

l = [2, 3, 0, 9]
# l.sort()
print(l)

print(sorted(l))

print(l)

l1 = [2, 3, 0, 9]
l2 = [12, [13, 10], 19]
l3 = l1 + l2
l1.extend(l2)

print(l3)

my_dict = {1: "Home", 2: "Office", 3: "Restaurant"}
for key, val in my_dict.items():
    print(f"{key} has value {val}")

v = my_dict.get(4, '**')
print(v)

l1 = [1, 2, 2, 3]
l2 = [1, 9, 2, 8]
print(l)

s1 = set(l1)
s2 = set(l2)

print(list(s1.intersection(s2)))
print(list(s1 - s2))
print(list(s1 | s2))
print(list(s1 & s2))
