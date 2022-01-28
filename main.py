import time
N = int(input('Введите количество циклопов N -> '))
s = input('Введите диоптрии в формате [x, y, ..., z], где x, y, z - числа.\n'
          'Кол-во диоптриев должно соответствовать кол-ву циклопов.\n'
          'После запятой ставится пробел-обязательно:')[1:-1]
D = s.split(', ')
D = [float(i) for i in D]
D.sort()
if len(D)!=N:
    print("Некорректный ввод, количество диоптриев не соответсвует количеству циклопов.\n "
          "Перезапустите программу и осуществите ввод заново!")
    exit(0)
NumCiklop = 0
num = 0
while NumCiklop < N:
    if NumCiklop+1 < N and (D[NumCiklop + 1] - D[NumCiklop]) <= 2:
        NumCiklop+=2

    else:
        NumCiklop+=1
    num+=1
print(f'Достаточно купить пар линз {num} ')
print('Консоль закроется через 10 секунд...')
time.sleep(10)
