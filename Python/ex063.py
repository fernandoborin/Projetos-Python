termos = int(input('Quantos termos você quer mostrar? '))
count = 0
fib1 = 0
fib2 = 1

while count < termos:
    
    fib3 = fib1 + fib2
    print(fib3)
    fib4 = fib3
    fib2 = fib1

    count += 1