import getpass
import os

from Carro import Carro
from Pessoa import Pessoa
from Venda import Venda

   # Autor/Author: Pedro Lucas de Oliveira Cabral
   # GitHub: https://github.com/DoisLucas
   # Data/Date: 04/05/2018

lista_carros = []
lista_pessoa = []
lista_venda = []

#Automatico
usuario = getpass.getuser()

#Manual
usuario = 'Pichau'

filepath = os.path.join('C:\\Users\\' + usuario + '\\Desktop\\', 'database.txt')

fileEscrita = open(filepath, "a+")
fileLeitura = open(filepath, "r+")

def menu():
    print("1) Cadastrar Carro")
    print("2) Listar Todos Carros")
    print("3) Excluir Carro")
    print("4) Alterar Carro")
    print("5) Cadastrar Pessoa")
    print("6) Listar Todas Pessoas")
    print("7) Excluir Pessoa")
    print("8) Alterar Pessoa")
    print("9) Realizar Venda")
    print("10) Mostar Vendas")
    print("11) Listar Carro de Pessoa")
    print("12) Sair")
    op = int(input("Opção: "))

    if (op == 1):

        pode = True
        numero_chassi = int(input("\nDigite o número do chassi do carro: "))

        for carros in lista_carros:
            if (carros.numero_chassi == numero_chassi):
                pode = False

        if (pode == True):

            nome = input("Digite o nome do carro: ")
            cor = input("Digite a cor do carro: ")
            ano = int(input("Digite o ano do carro: "))
            potencia = int(input("Digite a potencia do carro: "))
            valor = float(input("Digite o valor do carro: "))
            c = Carro(numero_chassi, nome, cor, ano, potencia, valor)
            lista_carros.append(c)
            print("\nCarro adicionado com sucesso!\n")

            escrever("carro;" + str(c.numero_chassi) + ';' + c.nome + ";" + c.cor + ";" + str(c.ano) + ";" + str(
                c.potencia) + ";" + str(c.valor) + "\n")
            menu()

        else:
            print("\nImpossivel cadastrar, número de chassi já em uso!\n")
            menu()

    elif (op == 2):

        if (lista_carros.__len__() != 0):
            print("\nLista Carros (", lista_carros.__len__(), ")")
            for carro in lista_carros:
                print("Numero Chassi: ", carro.numero_chassi, "\nNome: ", carro.nome, "\nCor: ", carro.cor,
                      "\nAno: ", carro.ano, "\nPotencia: ", carro.potencia, "\nValor: ", carro.valor, "\n")
        else:
            print("\nLista Vazia\n")

        menu()

    elif (op == 3):

        achou = False
        umavez = False;
        numero_chassi = int(input("\nDigite o numero do chassi para deletar o carro: "))

        for carro in lista_carros:
            if (carro.numero_chassi == numero_chassi):
                lista_carros.remove(carro)
                achou = True

        if (achou):

            linha_remove = None
            linha_dependeces = None

            lines = getLines()
            linha_remove = getLineObj('c', numero_chassi)

            for dependences in lines:
                if (dependences.split(";")[0] == "venda"):
                    if (numero_chassi == int(dependences.split(";")[2])):
                        linha_dependeces = dependences

            print(linha_dependeces)

            for vendas in lista_venda:

                if(linha_dependeces.split(";")[1].__eq__(str(vendas.pessoa.cpf))):
                    lista_venda.remove(vendas)

            line_entra = []

            if (not linha_dependeces == None):
                for line in lines:
                    if (not line.__eq__(linha_remove) and not line.__eq__(linha_dependeces)):
                        line_entra.append(line)
            else:
                for line in lines:
                    if (not line.__eq__(linha_remove)):
                        line_entra.append(line)

            limpar_arquivo()

            for line_e in line_entra:
                escrever(line_e)

            print("\nCarro Deletado com Sucesso! \n")

        else:
            print("\nCarro não existe!\n")

        menu()

    elif (op == 4):

        carro_achado = None
        numero_chassi = int(input("\nDigite o numero do chassi do carro para alterar: "))

        for carro in lista_carros:
            if (carro.numero_chassi == numero_chassi):
                carro_achado = carro

        if (carro_achado == None):
            print("\nCarro não existe!\n")
            menu()
        else:

            linha_remove = getLineObj('c', numero_chassi)

            print("\n\tAlterando carro: ", carro_achado.numero_chassi, " - ", carro_achado.nome, "\n")
            novo_nome = input("Digite o novo nome do carro: ")
            nova_cor = input("Digite a nova cor do carro: ")
            novo_ano = input("Digite o novo ano do carro: ")
            nova_potencia = input("Digite a nova potencia do carro: ")
            novo_valor = float(input("Digite o novo valor do carro: "))

            carro_achado.nome = novo_nome
            carro_achado.cor = nova_cor
            carro_achado.ano = novo_ano
            carro_achado.potencia = nova_potencia
            carro_achado.valor = novo_valor

            linha_add = 'carro;' + str(
                carro_achado.numero_chassi) + ';' + carro_achado.nome + ';' + carro_achado.cor + ';' + str(
                carro_achado.ano) + ';' + str(carro_achado.potencia) + ';' + str(carro_achado.valor)

            line_entra = []

            for line in getLines():

                if (not linha_remove == line):
                    line_entra.append(line)

            limpar_arquivo()

            for line_e in line_entra:
                escrever(line_e)

            escrever(linha_add + "\n")

            print("\nCarro alterado com sucesso!\n")
            menu()

    elif (op == 5):

        pode = True

        cpf = input("\nDigite o CPF da pessoa: ")

        for pessoas in lista_pessoa:
            if (pessoas.cpf == cpf):
                pode = False

        if (pode == True):
            nome = input("Digite o nome da pessoa: ")
            rg = input("Digite o RG da pessoa: ")
            idade = int(input("Digite a idade da pessoa: "))

            p = Pessoa(cpf, rg, idade, nome)
            lista_pessoa.append(p)

            print("\nPessoa Cadastrada com sucesso!\n")
            escrever("pessoa;" + p.cpf + ';' + p.rg + ";" + str(p.idade) + ";" + p.nome + "\n")
            menu()

        else:
            print("\nImpossivel cadastrar, CPF já em uso!\n")
            menu()

    elif (op == 6):

        if (lista_pessoa.__len__() != 0):
            print("\nLista de Pessoas (", lista_pessoa.__len__(), ")\n")
            for pessoa in lista_pessoa:
                print("Nome: ", pessoa.nome, end="")
                print("CPF: ", pessoa.cpf, "\nIdade: ", pessoa.idade, "\nRG: ", pessoa.rg,
                      "\n")
        else:
            print("\nLista vazia\n")
        menu()

    elif (op == 7):

        achou = False

        cpf = input("\nDigite o CPF da pessoa para deletar: ")

        for pessoa in lista_pessoa:
            if (pessoa.cpf == cpf):
                lista_pessoa.remove(pessoa)
                achou = True

        if (achou):

            lines = getLines()
            linha_remove = getLineObj('p', cpf)
            linha_dependeces = []

            for dependences in lines:
                if (dependences.split(";")[0] == "venda"):
                    if (cpf == dependences.split(";")[1]):
                        linha_dependeces.append(dependences)

            linha_dependeces.append(linha_remove)

            for dep in linha_dependeces:
                if(dep.split(";")[0] == "venda"):
                    for venda in lista_venda:
                        if(venda.pessoa.cpf == dep.split(';')[1]):
                            lista_venda.remove(venda)

            line_entra = []

            if (linha_dependeces.__len__() != 0):
                for i in lines:
                    if i not in linha_dependeces:
                        line_entra.append(i)
            else:
                for line in lines:
                    print(linha_remove, line)
                    if (not line.__eq__(linha_remove)):
                        line_entra.append(line)

            limpar_arquivo()

            for line_e in line_entra:
                escrever(line_e)

            print("\nPessoa Deletada com Sucesso! \n")

        else:
            print("\nPessoa não existe!\n")

        menu()

    elif (op == 8):

        pessoa_achada = None
        cpf = input("\nDigite o numero do CPF da pessoa para alterar: ")

        for pessoa in lista_pessoa:
            if (pessoa.cpf == cpf):
                pessoa_achada = pessoa

        if (pessoa_achada == None):
            print("Pessoa não existe!\n")
        else:

            lines = getLines()
            linha_remove = getLineObj('p', cpf)

            print("\n\tAlterando pessoa: ", pessoa_achada.cpf, " - ", pessoa_achada.nome, "\n")
            new_nome = input("Digite o novo nome: ")
            new_idade = input("Digite a nova idade: ")

            pessoa_achada.nome = new_nome
            pessoa_achada.idade = new_idade

            linha_add = "pessoa;" + pessoa_achada.cpf + ';' + pessoa_achada.rg + ";" + str(
                pessoa_achada.idade) + ";" + pessoa_achada.nome

            line_entra = []

            for line in lines:
                if (not linha_remove == line):
                    line_entra.append(line)

            limpar_arquivo()

            for line_e in line_entra:
                escrever(line_e)

            escrever(linha_add + "\n")

            print("\nPessoa Alterada com sucesso!\n")
            menu()

    elif (op == 9):

        cpf = input("\nDigite o CPF do comprador (Pessoa): ")
        numero_chassi = int(input("Digite o numero do chassi do carro para vender: "))

        pessoa_achada = None;
        carro_achado = None;

        for pessoa in lista_pessoa:
            if (pessoa.cpf == cpf):
                pessoa_achada = pessoa

        for carro in lista_carros:
            if (carro.numero_chassi == numero_chassi):
                carro_achado = carro

        if (pessoa_achada == None):
            print("\nPessoa não encontrada\n")
        else:
            if (carro_achado == None):
                print("\nCarro não encontrado\n")
            else:

                ja_vendido = False

                for venda in lista_venda:
                    if (carro_achado.numero_chassi == venda.carro.numero_chassi):
                        ja_vendido = True

                if (ja_vendido == False):

                    v = Venda(pessoa_achada, carro_achado)
                    lista_venda.append(v)
                    print("\nVenda realizada com sucesso!\n")

                    escrever("venda;" + str(pessoa_achada.cpf) + ';' + str(carro_achado.numero_chassi) + ";" + str(
                        v.data) + "\n")

                else:
                    print("\nCarro já foi vendido\n")

        menu()

    elif (op == 10):

        if (lista_venda.__len__() > 0):

            print("\nLista de vendas (", lista_venda.__len__(), ")")
            for venda in lista_venda:
                print("\nComprador: ", venda.pessoa.cpf, " - ", venda.pessoa.nome, "Carro: ", venda.carro.numero_chassi,
                      " - ", venda.carro.nome, "\n")
            menu()

        else:
            print("\nNenhuma venda encontrada!\n")
            menu()

    elif (op == 11):

        cpf = input("\nDigite o CPF da pessoa para listar carros: ")

        print("\nCarros: ")
        for venda in lista_venda:
            if (venda.pessoa.cpf == cpf):
                print("\n", venda.carro.numero_chassi, " - ", venda.carro.nome + '\n')

        menu()


def getLineObj(objeto, identificador):
    linha_remove = None
    lines = getLines()

    if (objeto == 'p'):
        for line in lines:
            if (identificador == line.split(";")[1] and line.split(";")[0] == "pessoa"):
                linha_remove = line

    elif (objeto == 'c'):
        for line in lines:
            if (identificador == int(line.split(";")[1]) and line.split(";")[0] == "carro"):
                linha_remove = line

    return linha_remove


def getLines():
    fileLeitura = open(filepath, "r+")
    lines = fileLeitura.readlines()
    fileLeitura.close()
    return lines


def limpar_arquivo():
    open(filepath, 'w').close()


def escrever(texto):
    fileEscrita = open(filepath, "a+")
    fileEscrita.write(texto)
    fileEscrita.close()


def reload():
    fileLeitura = open(filepath, "r+")
    lines = fileLeitura.readlines()
    fileLeitura.close()

    if (lines.__len__() != 0):
        print("\n\tCarregando DATABASE: (", lines.__len__(), ") objetos retornados\n")
        for obj in lines:
            lines_inside = obj.split(";")

            if (lines_inside[0] == "carro"):
                c = Carro(int(lines_inside[1]), lines_inside[2], lines_inside[3], lines_inside[4], lines_inside[5],
                          float(lines_inside[6]))

                lista_carros.append(c)
            elif (lines_inside[0] == "pessoa"):
                p = Pessoa(lines_inside[1], lines_inside[2], int(lines_inside[3]), lines_inside[4])
                lista_pessoa.append(p)

        for obj in lines:
            lines_inside = obj.split(";")
            if (lines_inside[0] == "venda"):

                pessoa_venda = None

                for pessoa in lista_pessoa:
                    if (pessoa.cpf == lines_inside[1]):
                        pessoa_venda = pessoa

                carro_venda = None

                for carro in lista_carros:
                    if (carro.numero_chassi == int(lines_inside[2])):
                        carro_venda = carro

                v = Venda(pessoa_venda, carro_venda)
                v.data = lines_inside[3]
                lista_venda.append(v)
                fileLeitura.close()

reload()
menu()