while True:
    switcher = int(input('Выберите режим конвертирования: '))
    value = float(input('Введите значение: '))
    if switcher == 0:
        break
    else:
        if switcher == 1:
            result = value * 2.54
            print(f'{value} inch. = {result} cm')
            # Дюймы в сантиметры
        if switcher == 2:
            result = value * 0.394
            print(f'{value} cm = {result} inch.')
            # Сантиметры в дюймы
        if switcher == 3:
            result = value * 1.61
            print(f'{value} ml = {result} km')
            # Мили в километры
        if switcher == 4:
            result = value * 0.621
            print(f'{value} km = {result} ml')
            # Километры в мили
        if switcher == 5:
            result = value * 0.4536
            print(f'{value} pds = {result} kg')
            # Фунты в килограммы
        if switcher == 6:
            result = value * 2.206
            print(f'{value} kg = {result} pds')
            # Килограммы в фунты
        if switcher == 7:
            result = value * 28.35
            print(f'{value} oun = {result} g')
            # Унции в граммы
        if switcher == 8:
            result = value * 0.0353
            print(f'{value} g = {result} oun')
            # Граммы в унции
        if switcher == 9:
            result = value * 4.55
            print(f'{value} gal = {result} l')
            # Галлон в литры
        if switcher == 10:
            result = value * 0.22
            print(f'{value} l = {result} gal')
            # Литры в галлоны
        if switcher == 11:
            result = value * 0,57
            print(f'{value} pints = {result} l')
            # Пинты в литры
        if switcher == 12:
            result = value * 1,76
            print(f'{value} l = {result} pints')
            # Литры в пинты
