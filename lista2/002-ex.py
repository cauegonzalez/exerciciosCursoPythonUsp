segundosStr = input('Por favor, entre com o número de segundos que deseja converter: ')
totalSegundos = int(segundosStr)

horasTotal = totalSegundos // 3600
dias = horasTotal // 24
horas = horasTotal % 24

segundosRestantes = totalSegundos % 3600
minutos = segundosRestantes // 60
segundos = segundosRestantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos")

