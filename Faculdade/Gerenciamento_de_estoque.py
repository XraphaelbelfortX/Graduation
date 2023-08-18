# Dicionário para armazenar as informações dos produtos
import os
estoque = []
i = 0
valor_minimo = 10

# Entrada
while True:
    print('Deseja abrir sistema?')
    opcao_inicial = input('[s]im [n]ão: ')
    print('-----------------------')

    if opcao_inicial == 'n':
        print('Sistema Fechado')
        break

    else:
        print('Selecione uma opção')
        opcao = input('[e]ntrada [a]pagar [c]onsulta [f]echar: ')

# Declarar o valor mínimo permitido em estoque por categoria
        VALOR_MINIMO_POR_CATEGORIA = {
        "1": 10,
        "2": 10,
        "3": 10,
    # Adicione mais categorias e valores mínimos conforme necessário
}
# Criando Sistema de EScolhas
        if opcao == 'e':
            num_registros = int(input("Quantos produtos deseja registrar? "))
            for _ in range(num_registros):
                nome_produto = input("Digite o nome do produto: ")
                print('-----------------------')
                categoria_produto = input("[1]Artigo Esportivo [2]Periféricos [3]Moda: ")
                quantidade_produto = int(input("Digite a quantidade de produtos: "))
                if quantidade_produto < valor_minimo:
                    print('Adicione uma maior quantidade')
                    quantidade_produto = int(input('Digite a quantidade de produtos: '))
                    estoque.append({"nome": nome_produto, "categoria": categoria_produto, "quantidade": quantidade_produto})
                    print('Produto Registrado!')
                    print('-----------------------')
                else:
                    estoque.append({"nome": nome_produto, "categoria": categoria_produto, "quantidade": quantidade_produto})
                    print('Produto Registrado!')
                    print('-----------------------')

        
        elif opcao == 'a':
            indice_str = input('Escolha o índice para apagar: ') 
        
            try:
                indice = int(indice_str)
                del estoque[indice]
            except ValueError:
                print('Não foi possível apagar esse índice')
            except IndexError:
                print('Índice não existe na lista')
            except Exception:
                print('Erro desconhecido')

        if opcao == 'f':
            print('Sistema Finalizado!')
            break
        
        if opcao == 'c':
            os.system('cls')
            

            for i, nome_produto in enumerate(estoque):
                print(i, estoque)
                print('--------------------------------------------------------')
# Função para calcular o quantitativo total de produtos em estoque
                def calcular_quantidade_total():
                    total_quantidade = 0
                    for item in estoque:
                        total_quantidade += item["quantidade"]
                        return total_quantidade


# Função para apresentar a porcentagem de estoque por categoria
                def apresentar_porcentagem_estoque():
                    for categoria in VALOR_MINIMO_POR_CATEGORIA:
                        quantidade_categoria = sum(item["quantidade"] for item in estoque if item["categoria"] == categoria)
                        valor_minimo = VALOR_MINIMO_POR_CATEGORIA[categoria]
                        porcentagem = (quantidade_categoria / valor_minimo) * 100
                        print(f"Porcentagem de estoque para a categoria '{categoria}': {porcentagem:.2f}%")
                        print('--------------------------------------------------------')

# Registrar duas entradas de produtos


# Calcular o quantitativo total de produtos em estoque
                quantidade_total = calcular_quantidade_total()
                print(f"Quantidade total de produtos em estoque: {quantidade_total}")
                print('--------------------------------------------------------')

# Apresentar a porcentagem de estoque por categoria
                apresentar_porcentagem_estoque()


        




