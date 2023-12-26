import csv

def criar_contato(nome, telefone, email):
    return [nome, telefone, email]

def adicionar_contato(contato):
    with open('contatos.csv', mode='a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(contato)

def remover_contato(nome):
    contatos = carregar_contatos()
    contatos = [contato for contato in contatos if contato[0] != nome]
    salvar_contatos(contatos)

def pesquisar_contato(nome):
    contatos = carregar_contatos()
    resultados = [contato for contato in contatos if contato[0] == nome]
    return resultados

def carregar_contatos():
    with open('contatos.csv', mode='r') as arquivo:
        reader = csv.reader(arquivo)
        contatos = [contato for contato in reader]
        return contatos

def salvar_contatos(contatos):
    with open('contatos.csv', mode='w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(contatos)

# Exemplo de uso:
contato1 = criar_contato('João', '123456789', 'joao@example.com')
contato2 = criar_contato('Maria', '987654321', 'maria@example.com')

adicionar_contato(contato1)
adicionar_contato(contato2)

contatos = carregar_contatos()
print(contatos)

remover_contato('Maria')

contatos = pesquisar_contato('João')
print(contatos)
