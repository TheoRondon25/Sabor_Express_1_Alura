

# ___________________________________

# frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
# contagem_palavras = {}
# palavras = frase.split()
# for palavra in palavras:
#     contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
# print(contagem_palavras)

# ___________________________________

# pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
# if 'nome' in pessoa:
#     print("A chave 'nome' existe no dicionário.")
# else:
#     print("A chave 'nome' não existe no dicionário.")

# ___________________________________

# numeros_quadrados = {x: x**2 for x in range(1, 6)}
# print(numeros_quadrados)

# ___________________________________

# pessoa = {'nome':'Theo', 'idade':20, 'cidade':'Bauru'}

# pessoa['idade'] = 21 
# pessoa['profissao'] = 'Programador'
# pessoa.pop('cidade') ou del pessoa['cidade']
# print(pessoa)

# ___________________________________

# lista = []
# soma = 0
# ocorreu_erro = False

# for numero in lista:
#     soma += numero
# try: 
#     media = soma/len(lista)
# except ZeroDivisionError:
#     ocorreu_erro = True
#     print('Lista vazia ou dividiu por ZERO!') 

# if not ocorreu_erro:
#     print(f'Média = {media}')
    
# ___________________________________

# numeros = [10, 20, 30, 40, 'a']
# soma = 0
# ocorreu_erro = False
# for numero in numeros:
#     try: 
#         soma += numero
#         print(f'Soma agora = {soma}')
#     except Exception as e: 
#         print(f'Houve um erro! -> {e}')
#         ocorreu_erro = True
#         break
    
# if not ocorreu_erro:
#     print(f'\nSoma Final = {soma}')

# ___________________________________

# numero_inserido = int(input('Digite o número que quer saber a tabuada: '))
# num = 0
# for i in range(1, 11):
#     num += 1
#     print(f'{numero_inserido}x{num}={num*numero_inserido}')

# ___________________________________

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for numero in lista[::-1]:
#     print(numero)

# ___________________________________

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# soma_impar = 0

# for i in lista:
#     if i % 2 != 0:
#         soma_impar += i 
        
# print(soma_impar)

# ___________________________________

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in lista:
#     print(i)

# ___________________________________

# x = float(input('Digite a coordenada x: '))
# y = float(input('Digite a coordenada y: '))

# if x > 0 and y > 0:
#     print('Primeiro Quadrante')
# elif x < 0 and y > 0:
#     print('Segundo Quadrante')
# elif x < 0 and y < 0:
#     print('Terceiro Quadrante')
# elif x > 0 and y < 0:
#     print('Quarto Quadrante')
# else:
#     print('o ponto está localizado no eixo ou origem!') 

# ___________________________________

# login_correto = 'theorondon'
# senha_correta = 'theo25'

# login = input('Digite seu login: ')
# senha = input('Digite a senha: ')

# if login == login_correto and senha == senha_correta:
#     print('entrou no programa!')
# else: 
#     print('login ou senha incorretos')

# ___________________________________

# idade = int(input('Digite sua idade: '))

# if idade <= 12:
#     print('CRIANÇA')
# elif 13 <= idade <= 18:
#     print('ADOLESCENTE')
# else: 
#     print('ADULTO')

# ___________________________________

# numero = int(input('Insira um numero: '))

# if numero % 2 == 0:
#     print(f'{numero} é PAR')
# else:
#     print(f'{numero} é IMPAR')

# ___________________________________

# pi = 3.14159

# print(f'O valor arredondado de pi é: {pi:.2f}')

# ___________________________________

# palavra = 'ALURA'

# for letra in palavra:
#     print(f'{letra}\n')

