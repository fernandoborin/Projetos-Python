# Faz a sequência de Fibonacci até o termo digitado

numtermos = int(input('Quantos termos você quer mostrar? '))
count = 0
fib1 = 0
fib2 = 1

while count < numtermos - 2:
    if count == 0:
        print(fib1)
        print(fib2)
    fib3 = fib1 + fib2
    print(fib3)
    fib1 = fib2
    fib2 = fib3

    count += 1