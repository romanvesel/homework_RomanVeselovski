some_list = [1, 2, 3, 4, 5]
new_some_list = some_list[1:] + some_list[:1]
print(new_some_list)

# Только через while смог.

some_list[0] = some_list[-1]
i = len(some_list) - 1
while i > 0:
    some_list[i] = some_list[i - 1]
    i -= 1
some_list[1] = 1
print(some_list)