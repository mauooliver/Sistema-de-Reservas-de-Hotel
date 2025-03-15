# - ***Desafio 2:  Condicionais***
# ***Sistema de Reservas de Hotel:***
# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.
# - *Cadastro de Cliente:*
# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*
# - *Reservas de Quartos:*
# ***O sistema deve oferecer 3 tipos de quartos:*** 
# ***"Simples", "Duplo" e "Luxo".***
# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***
# - ***Cálculo da Estadia:***
# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***
# Exemplo: 
#  ***valor_cliente3 = preco_duplo * cliente3_dias***
# *Pagamento:*
# *O sistema deve exibir o valor total a ser pago por cada cliente após a aplicação do desconto.*
# *Regras Adicionais:
# Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*
# ***O sistema não deve usar loops (for, while) nem funções.**
# O código deve considerar todos os casos possíveis de escolha dos clientes.*

print(' Seja bem vindo(a): A rede Hoteis.com, acodando sonhos')
print('---' * 9)
print('Informe seus dados, para continuar')
print('---' * 9)
cliente1_nome = input('Digite seu nome: ')
cliente1_idade = int(input('Digite sua idade: '))
cliente2_nome = input('Digite seu nome: ')
cliente2_idade = int(input('Digite sua idade: '))
cliente3_nome = input('Digite seu nome: ')
cliente3_idade = int(input('Digite sua idade: '))

lista_quartos = ['Simples (0)' , 'Duplo (1)' , 'Luxo (2)']
lista_preços  = [  100.00  ,  150.00 , 250.00]

print('---' * 9)
print(lista_quartos)

print('---' * 9)
escolha1_quarto = int(input('Qual quarto o senhor deseja? Cliente1: '))
escolha2_quarto = int(input('Qual quarto o senhor deseja? Cliente2: '))
escolha3_quarto = int(input('Qual quarto o senhor deseja? Cliente3: '))
print('---' * 9)
qtd_dias_cliente1 = int(input('Por quantos dias o senhor deseja se hospedar?  '))
qtd_dias_cliente2 = int(input('Por quantos dias o senhor deseja se hospedar?  '))
qtd_dias_cliente3 = int(input('Por quantos dias o senhor deseja se hospedar?  '))
print('---' * 9)
reserva_cliente1 = lista_preços[escolha1_quarto] * qtd_dias_cliente1
reserva_cliente2 = lista_preços[escolha2_quarto] * qtd_dias_cliente2
reserva_cliente3 = lista_preços[escolha3_quarto] * qtd_dias_cliente3
print('---' * 9)
print('O Hospede', qtd_dias_cliente1, 'Escolhou a acomodação', lista_quartos[escolha1_quarto])
print('O Hospede', qtd_dias_cliente2, 'Escolhou a acomodação', lista_quartos[escolha2_quarto])
print('O Hospede', qtd_dias_cliente3, 'Escolhou a acomodação', lista_quartos[escolha3_quarto])
print('---' * 9)

print('Reserva do cliente', cliente1_nome,'R$', reserva_cliente1)
print('Reserva do cliente', cliente2_nome,'R$', reserva_cliente2)
print('Reserva do cliente', cliente3_nome,'R$', reserva_cliente3)
print('---' * 9)

print('Obrigado por escolhaer nossas acomodações, Hoteis.com Agradece.')



