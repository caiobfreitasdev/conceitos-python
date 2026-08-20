import os


restaurante = [
    {"nome": "Sushi Graudo", "categoria": "Japonesas", "ativo": False},
    {"nome": "Pizza do Pizzaiolo", "categoria": "Massas", "ativo": True},
    {"nome": "Manjericão", "categoria": "Frutos do Mar", "ativo": True},
    {"nome": "Carne Du Dudu", "categoria": "Churrascaria", "ativo": True},
    ]
                

def voltar_menu_principal():
    while True:
        voltar = input("Deseja voltar ao menu principal? (S/N): \n").strip().upper()
        if voltar == "S":
            main()
            return
        elif voltar == "N":
            finalizar_app()
            return
        else:
            print("Digite uma opção válida:")

def alternar_estado_restaurante():
    print("Alterando estado do restaurante")
    nome_procurado = input("Digite o nome do restaurante que deseja alterar o estado: ").strip()
    restaurante_encontrado = False

    for item in restaurante:
        if item["nome"] == nome_procurado:
            restaurante_encontrado = True
            item["ativo"] = not item["ativo"]
            if item["ativo"]:
                mensagem = f"O restaurante {nome_procurado} foi ativado com sucesso"
            else:
                mensagem = f"O restaurante {nome_procurado} foi desativado com sucesso"
            print(mensagem)
            break
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_menu_principal()

def exibir_nome():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n"""
)

def finalizar_app():
    os.system('cls')
    print("Finalizando o app")

def opcao_invalida():
    print("Opção Inválida!")
    voltar_menu_principal()

def lista_restaurantes():
    os.system("cls")
    print("Listar restaurantes:")
    for item in restaurante:
        nome = item["nome"]
        categoria_restaurante = item["categoria"]
        ativo_restaurante = item["ativo"]
        print(f".{nome} | {categoria_restaurante} | {ativo_restaurante}")
    voltar_menu_principal()            

def cadastrar_novo_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes \n")
    nome_do_restaurante = input("Digite o nome do Restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "categoria": categoria,
        "ativo": False 
        }
    restaurante.append(dados_do_restaurante)
    print(f"O Restaurante {nome_do_restaurante}, foi cadastrado com sucesso!")
    voltar_menu_principal()

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")
    


def selecionar_opcao_programa():
    try:
        selecionar_opcao = int(input("Selecione a opção: "))
        print("\n")
        if selecionar_opcao == 1:
            print("1. Cadastrar restaurante")
            cadastrar_novo_restaurante()
        elif selecionar_opcao == 2:
            lista_restaurantes()
        elif selecionar_opcao == 3:
            alternar_estado_restaurante()
        elif selecionar_opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome()
    exibir_opcoes()
    selecionar_opcao_programa()
    
    

if __name__ == '__main__':
    main()