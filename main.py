# Вычислить количество рулонов обоев для комнаты
a = float(input('Введите длину помощения: ')) * 2
b = float(input('Введите ширину помощения: ')) * 2
c = float(input('Введите высоту стен в помощении: '))
d = float(input('Введите длину рулона обоев: '))
e = float(input('Введите ширину рулона обоев: '))
total1 = (a + b) * c
total2 = d * e
print('Необходимо приобрести', (total1 - 1) // total2 + 1, 'рулонов обоев')
