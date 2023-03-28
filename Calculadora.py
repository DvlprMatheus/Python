# Faça uma calculadora simples utilizando Python

numero1 = 0
numero2 = 0
operacao = ''
resultado = 0

numero1 = int(input('Digite o primeiro número: '))
operacao = input('Digite a operação: ')
numero2 = int(input('Digite o segundo número: '))

if operacao == "+" :
    resultado = (numero1 + numero2)
elif operacao == "-" :
    resultado = (numero1 - numero2)
elif operacao == "*" :
    resultado = (numero1 * numero2)
elif operacao == "x" :
    resultado = (numero1 * numero2)
elif operacao == "/" :
    resultado = (numero1 / numero2)
elif operacao == "÷" :
    resultado = (numero1 / numero2)

print(resultado)