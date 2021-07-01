import random
from copy import deepcopy

elements = [x for x in range(11)]

# print(choices)

while True:
    random_choice = random.choice(elements)
    if random_choice % 3 == 0:
        break
    print(f"Random choice is {random_choice}")
print(f"Exit random choice is {random_choice}")

for i in range(11):
    if i % 2 != 0:
        continue
    print(f"Numar par : {i}")

my_sum = 0


def get_sum(a, b):
    global my_sum
    my_sum = a + b;
    print(my_sum)


get_sum(1, 2)
print(my_sum)

l1 = [1, 2, 3, [2, 3, 4]]

l2 = deepcopy(l1)
# l2 = l1.copy()
# l2 = list(l1)
# l2 = [x for x in l1]

l2[3].append(5)

print(l1)
print(l2)


def my_func(nume, prenume, *args, **kvargs):
    tail = " ".join(args)
    print(f"{nume} {prenume} {tail}")
    for key in kvargs.keys():
        print(f"key : {key} has value {kvargs[key]}")


my_func("popescu", "ana", "are", '3', "mere", job='developer', age=22)

print(dir(__builtins__))
