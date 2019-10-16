Sec = input('Digite o valor em segundos a ser convertido: ')

Sec = int(Sec)

Hr = Sec // 3600
HrR = Sec % 3600
Min = Sec // 60
SecR = Sec % 60

while (Hr > 24):
    Day = 0
    Hr = Hr - 24
    Day = Day + 1

print(Day, 'dias, ', Hr, 'horas, ', Min, 'minutos e ', SecR, 'segundos')