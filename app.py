import os 

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False},]


def exibir_nome_do_programa():
    '''Essa função é responsavel por exibir o nome do nosso projeto na execução'''
    print('𝘚𝘢𝘣𝘰𝘳 𝘌𝘹𝘱𝘳𝘦𝘴𝘴\n')

def exibir_opcoes():
    '''Essa função é responsavel por exibir as opçoes que temos dentro do programa'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função é responsavel por finalizar o programa'''
    exibir_subtitulo('Encerrando o app')

def voltar_ao_menu_principal():
    '''Essa função é responsavel por voltar ao menu no final da execução de alguma opção'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Essa função é responsavel por mostrar o erro de opção inválida e voltar ao menu principal após isso'''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsavel por exibir o titulo da opçao escolhida em sua execuçao'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante na lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com suceso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa funçao é responsavel por listar os restaurantes quando executada a opçao Listar Restaurantes'''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurando'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa funçao é responsavel por alternar os status dos restaurantes quando executada a opçao Ativar Restaurantes'''
    exibir_subtitulo('alterando estado do restaurante')

    nome_restaurante = input('Dgite o nome do restaurante que deseja alterar o estado: ')    
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa funçao é responsavel por puxar as funçoes das opçoes escolhidas pelo usuario'''
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função organiza a sequência inicial de execução do programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()  