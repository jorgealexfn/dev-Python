contatos= []

def adicionar_contato(nome, telefone):
    contato = {"Nome" : nome, "Telefone": telefone}
    contatos.append(contato)
    print("Contato adicionado com Sucesso")

def listar_contatos():
    if not contatos:
        print("Não há contatos cadastrados...")
    else:
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def buscar_contato(nome):
    if not contatos:
        print("Não há contatos cadastrados.")
        return
    for contato in contatos:
        if contato["nome"] == nome:
            print(f"Contato encontrado: {contato['nome']}, Telefone: {contato['telefone']}")
            return
    print("Contato não encontrado...")

def excluir_contato(nome):
    if not contatos:
        print("Não há contatos cadastrados.")
        return
    for i, contato in enumerate(contatos):
        if contato["nome"] == nome:
            del contatos[i]
            print("Contato excluido com sucesso!")
            return


# Loop principal do programa
while True:
    print("""
          ################################
          ********************************
          ################################


          1. Adicionar contato
          2. Listar contatos
          3. Buscar contato
          4. Excluir contato
          5. Sair


          ################################
          ********************************
          ################################
          
          """)


    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefoner: ")
        adicionar_contato(nome, telefone)
    elif opcao == 2:
        listar_contatos()
    elif opcao == 3:
        nome = input("Digite o nome para buscar: ")
        buscar_contato()
    elif opcao == 4:
        nome = input("Digite o nome para exluir: ")
        excluir_contato()
    elif opcao == 5:
        break
    else:
        print("Opção inválida.")