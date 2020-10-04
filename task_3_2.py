some_guests = input ('Enter number of guests: ')
some_guests = int(some_guests)
if some_guests > 50:
    print ('need a restaurant')
elif 20 <= some_guests <= 50:
    print ('need a cafe')
else:
    print ('celebrate at home')