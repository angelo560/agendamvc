from model import Contato, Agenda


class AgendaController:
    def __init__(self):
        self.agenda = Agenda()

    def adicionar(self):
        print("\n- ADICIONAR CONTATO -")

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        grupo = input("Grupo: ")

        contato = Contato(nome, telefone, email, grupo)

        self.agenda.adicionar_contato(contato)

        print("\nContato adicionado com sucesso!")

    def listar(self):
        print("\n- LISTA DE CONTATOS -")

        contatos = self.agenda.listar_contatos()

        if len(contatos) == 0:
            print("Nenhum contato cadastrado.")
        else:
            for contato in contatos:
                print("------------------------")
                print("Nome:", contato.nome)
                print("Telefone:", contato.telefone)
                print("Email:", contato.email)
                print("Grupo:", contato.grupo)

    def buscar(self):
        print("\n- BUSCAR CONTATO -")

        nome = input("Digite o nome: ")

        contato = self.agenda.buscar_contato(nome)

        if contato != None:
            print("\nContato encontrado:")
            print("Nome:", contato.nome)
            print("Telefone:", contato.telefone)
            print("Email:", contato.email)
            print("Grupo:", contato.grupo)
        else:
            print("Contato não encontrado.")

    def remover(self):
        print("\n- REMOVER CONTATO -")

        nome = input("Digite o nome do contato: ")

        resultado = self.agenda.remover_contato(nome)

        if resultado == True:
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")

    def listar_grupo(self):
        print("\n--- CONTATOS POR GRUPO ---")

        grupo = input("Digite o grupo: ")

        contatos = self.agenda.listar_por_grupo(grupo)

        if len(contatos) == 0:
            print("Nenhum contato nesse grupo.")
        else:
            for contato in contatos:
                print("------------------------")
                print("Nome:", contato.nome)
                print("Telefone:", contato.telefone)
                print("Email:", contato.email)
                print("Grupo:", contato.grupo)

    def menu(self):
        opcao = ""

        while opcao != "6":
            print("\n- AGENDA -")
            print("1 - Adicionar contato")
            print("2 - Listar contatos")
            print("3 - Buscar contato")
            print("4 - Remover contato")
            print("5 - Listar contatos por grupo")
            print("6 - Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.adicionar()

            elif opcao == "2":
                self.listar()

            elif opcao == "3":
                self.buscar()

            elif opcao == "4":
                self.remover()

            elif opcao == "5":
                self.listar_grupo()
