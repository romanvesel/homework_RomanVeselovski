dct = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key, value in list(dict.items(dct)):
    new_key = key + str(len(key))
    new_dct = {new_key:value}
    print(new_dct)



# Как это сделать через while???



