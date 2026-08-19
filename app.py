import os


restaurante = ["Pizza", "Café"]

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
    voltar_menu = input("Deseja voltar ao menu principal? (S/N): \n")
    if voltar_menu == "S":
        main()
    elif voltar_menu == "N":
        finalizar_app()

def lista_restaurantes():
    os.system("cls")
    print("Listar restaurantes:")
    for nome in restaurante:
        print(f".{nome}")
    voltar_menuv3 = input("Deseja voltar ao menu principal? (S/N)\n")
    if voltar_menuv3 == "S":
        main()
    else:
        finalizar_app

        
        

def cadastrar_novo_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes \n")
    nome_do_restaurante = input("Digite o nome do Restaurante que deseja cadastrar: ")
    restaurante.append(nome_do_restaurante)
    print(f"O Restaurante {nome_do_restaurante}, foi cadastrado com sucesso!")
    voltar_menu2 = input("Deseja cadastrar um novo restaurante ? (S/N)\n")
    if voltar_menu2 == "S":
        cadastrar_novo_restaurante()
    else:
        main()

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
        elif selecionar_opcao ==2:
            lista_restaurantes()
        elif selecionar_opcao ==3:
            print("3. Ativar restaurante")
        elif selecionar_opcao ==4:
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