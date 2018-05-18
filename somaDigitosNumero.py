numero = int(input('Digite um número para que seus dígitos sejam somados: '))
soma = 0

while numero != 0:
    soma = soma + (numero % 10)
    numero = numero // 10

print('A soma dos dígitos do número digitado é:', soma)