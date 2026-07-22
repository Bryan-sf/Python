Estoque = {
    1: {'nome': 'Maça', 'valor': 10.00, 'estoque': 3},
    2: {'nome': 'Banana', 'valor': 5.00, 'estoque': 4},
    3: {'nome': 'Chinelo', 'valor': 25.00, 'estoque': 2},
}

#parte visual do estoque (onde vai mostrar os produtos pro cliente)
def mostrar_estoque():
    global estoque_total
    estoque_total = 0


    print('\n\t\t~ PRODUTOS~\n')
    print('-'*50)

    for produto in Estoque:
        print(f'{produto:<3} {Estoque[produto]["nome"]:<10} |preço: {Estoque[produto]["valor"]:<8} |estoque: {Estoque[produto]["estoque"]}')
        estoque_total += Estoque[produto]['estoque']

    print('-'*50)

#local onde cadastra um novo produto
def cadastrar_produto():
    novo_id = max(Estoque.keys()) + 1  # pega o proximo id disponivel
    nome = input('Nome do produto: ')
    valor = float(input('Valor: '))
    qtd = int(input('Quantidade em estoque: '))
    
    Estoque[novo_id] = {'nome': nome, 'valor': valor, 'estoque': qtd}
    print(f'Produto "{nome}" cadastrado com id {novo_id}')

#funçao para editar o produto
#def editar_produto():

#funçao para apagar o produto
#def apagar_produto():


#para quando o usuario afirma ser um funcionario
def menu_funcionario():
    while True:
        print('\n1 - Ver estoque')
        print('2 - Cadastrar produto')
        print('3 - Editar produto')
        print('4 - Apagar produto')
        print('0 - Sair')
        
        opcao = input('Escolha: ')
        
        if opcao == '1':
            mostrar_estoque()
        elif opcao == '2':
            cadastrar_produto()
        elif opcao == '0':
            break
        else:
            print('opcao invalida.')
        

 

#funçao para o menu cliente
def menu_cliente():
#momento da compra
    global estoque_total
    mostrar_estoque()
    soma = 0

    while True:
        try:
            resposta = int(input('\nO que deseja comprar? (digite o id, ou digite 0 para sair):\n'))
        except ValueError: 
            print('Digite um numero valido por favor.')
            continue
            
        #carrinho de compras
        if resposta == 0:
            break
        
        if estoque_total == 0:
            print('O estoque da loja acabou por hoje :(')
            break
        elif resposta not in Estoque:
            print('Produto nao encontrado.')
        elif Estoque[resposta]['estoque'] <= 0:
            print(f'\nO estoque de "{Estoque[resposta]['nome']}" nao esta disponivel.')
        
        else:
            id_ = resposta
            soma += Estoque[id_]['valor']
            Estoque[id_]['estoque'] -= 1
            estoque_total -= 1
            
            print(f'\nO valor da compra esta em: {soma}')
            print(f'Estoque atual de {Estoque[id_]['nome']}: {Estoque[id_]['estoque']}')
        
        #resposta = int(input('\n\nDeseja comprar novamente? (digite o id, ou digite 0 para sair):\n'))


    #valor total da compra    
    print(f'\nE o valor total da compra foi: {soma}\n')
    

def menu_principal():

    while True:
        try:
            
            resposta = int(input('| 1 - cliente\n| 2 - funcionario\n| 0 - sair\nQuem esta acessando?:'))
            
            if resposta == 1:
                menu_cliente()
            elif resposta == 2:
                menu_funcionario()
            elif resposta == 0:
                break
            
        except ValueError:
            print('Resposta invalida. Insira apenas 1 ou 2.')

menu_principal()
