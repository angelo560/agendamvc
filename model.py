class Contato:
    def __init__(self, nome, telefone, email, grupo):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.grupo = grupo


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        return self.contatos

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                return contato

        return None

    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)

        if contato != None:
            self.contatos.remove(contato)
            return True

        return False

    def listar_por_grupo(self, grupo):
        contatos_grupo = []

        for contato in self.contatos:
            if contato.grupo.lower() == grupo.lower():
                contatos_grupo.append(contato)

        return contatos_grupo
