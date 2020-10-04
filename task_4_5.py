fibonachi = []
total_numbers = int(input('Enter total numbers: '))
for x in range(int(total_numbers)):
    if x == 0:
        fibonachi.append(int(0))
    elif x == 1:
            fibonachi.append(int(1))
    elif x == 2:
            fibonachi.append(int(2))
    else:
        while len(fibonachi) < total_numbers:
            fibonachi.append(int((fibonachi[-1] + fibonachi[-2])))
print(fibonachi)

#Использовал два разных в одном задании.
