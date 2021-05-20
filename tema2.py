my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Sortare crescatoare")
print(sorted(my_list))
print("Sortare descrescatoare")
print(sorted(my_list, reverse=True))
print("Numerele pare")

even_list = my_list[1:4:2]
even_list.append(my_list[6])
even_list.extend(my_list[-3::2])

print(even_list)

print("Numere impare")
odd_list = my_list[:5:2]
odd_list.extend(my_list[5:-1:3])
print(odd_list)

# alta metoda , dar care implica si o sortare
print("numere pare")
sorted_list = sorted(my_list)
even_list = sorted_list[1::2]
print(even_list)

print("numere impare")
odd_list = sorted_list[::2]
print(odd_list)

print("%3")
mul3 = [];
for x in my_list:
    if x % 3 == 0:
        mul3.append(x)
print(mul3)



