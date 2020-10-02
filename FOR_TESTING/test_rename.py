import random
import os
import string

arr = []

for i in range(1, 5):
    temp = random.randint(1, 10)
    arr.append(temp)


# values = "".join(x for x in arr)
values = "".join(map(str, arr))

print('INT')
print(values)


ab = string.digits + string.ascii_letters
name = []

for x in range(1,20):
    anu = random.choice(ab)
    name.append(anu)

# val = "".join(map(str, name))
val = "".join(str(x) for x in name)

print('\n')
print('STRING')
print()
hasil = os.path.devnull+ '/' + val + '.jpg'
print(hasil)
print()
print(hasil.split('.'))
