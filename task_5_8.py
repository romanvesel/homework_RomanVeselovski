a = input('Enter your text: ')
some_list = a.split(' ')

new_list = [i[::-1] for i in some_list]

print(new_list)