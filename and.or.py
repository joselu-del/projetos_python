numero = float(input("Digite um numero de 0 a 10:"))
dia = str(input("Digite o dia da semana:"))

if numero == 1 and dia == "segunda":
    print("Segunda, horario da manhã!")
    
elif numero == 2 or numero == 3:
    print("Este é o horario da tarde")
    
else:
    print("Voce digitou o numero errado")

    