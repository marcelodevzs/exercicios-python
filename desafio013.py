print('====== DESAFIO 013 ======')
print()
print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')
print()
salario = float(input('Digite seu salário : '))
aumento = salario / 20
ns = aumento * 3
print()
print('Seu novo salário com 15% de aumento agora é R$ {:.2f}.'.format(salario+ns))
print()
print('Criado por : Marcelo Augusto')
