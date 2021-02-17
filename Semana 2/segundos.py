# Programa para conversão de segundos em dias, horas, minutos e segundos
s = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = s // 86400 # Dias = resultado da divisão inteira de segundos por total de segundos de um dia
segundosDias = s % 86400 # segundosDias = Resto da divisão dos segundos pelo total de segundos de um dia
horas = segundosDias // 3600 # horas = resultado da divisão inteira de segundosDias pelo total de segundos em uma hora
segundosHoras = segundosDias % 3600 # segundosHoras = Resto da divisão dos segundosDias pelo total de segundos de uma hora
minutos = segundosHoras // 60 # ...
segundosMinutos = segundosHoras % 60 # ...

print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundosMinutos} segundos.')