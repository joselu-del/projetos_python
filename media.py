# Primeira parte é a difinição do "problema"
# Problema: solicitar 4 notas de determinado aluno, após isso, calcular a média, com isso, definir a aprovação, reprovação e mais alguma mensagem, caso seja necessário
# Solicita as três notas do aluno
nota1 = float(input("Digite a primeira nota:"))         #definimos as váriaveis: 4 notas
nota2 = float(input("Digite a segunda nota:"))          #float: usamos pra que o python receba número com casa decimal
nota3 = float(input("Digite a terceira nota:"))         #input usada para declarar que a variavel ira receber um dado
nota4 = float(input("Digite a quarta nota:"))


# Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4             #definimos o calculo aritmetico: média 

print(f"\nMédia final: {media}")                        #após definimos o calculo, precisamos printala na tela, seguida de alguma mensagem, caso for necessário 

# Avaliação do desempenho
if media >= 9.0:                                           #Botamos a primeira condição usando if, seguido de uma mensagem caso seja dentro desta amostra
    print("Desempenho: Excelente! 🏆\n Aprovado!")
elif media >= 7.0:                                          #usamos o elif a fim de economizar memória e finalizar o processo caso seja o 9.0 ou 7.0                 
    print("Desempenho: Bom! 👍\n Aprovado!")
elif media >= 5.0:
    print("Desempenho: Regular. 😐\n Reprovado")
else:                                                       #usamos o else a fim de finalizar a busca caso as alternativas anteriores não sejam atendidades
    print("Desempenho: Insuficiente. 😞\n Reprovado")

