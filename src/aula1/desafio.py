#Escrever um programa em PYhton que solicita para o usuario digitar seu nome, o valor sdo seu salario e o valor do bonús que recebeu 
#O program deve entao imprimir uma mensagem saudando o usuário pelo nome e imformar o valor do salario em comparação com o bonus recebido.

nome = input('Qual seu nome: ')
valor_salario = float(input('Digite o valor do salario recebido: '))
porcentagem_bonus = float(input('Digite a porcentagem do bonus: '))

calculos = 1000 + valor_salario * porcentagem_bonus

print(f'Olha {nome}, tudo bem? \nire mostrar o valor do seu bonus.')
print(f'Seu bonus e {calculos}')