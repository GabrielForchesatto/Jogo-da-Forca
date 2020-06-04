def linha():
    print('-=' * 10)
import os

def string(value): #Valida para que a entrada seja apenas letras, sem números

    if value.isalpha() == True:
        return True
    else:
        return False


def asteriscos(palavra):
    return print("*" * len(palavra))


def Desafiante():

    while True: #Verifiador dos dados dos usuários

        Desafiante = str(input('Desafiante: ').strip().upper())
        if Desafiante != '':
            break
        if Desafiante == '': #Evita nomes vazios
            print("O nome está vazio, informe novamente")


    return Desafiante


def Competidor():
    while True: #Verifiador dos dados dos usuários
        Competidor = ''
        Competidor = str(input('Competidor: ').strip().upper())
        if Competidor!= '':
            break
        if Competidor == '': #Evita nomes vazios
            print("O nome está vazio, informe novamente")

    return Competidor


def Palavra_chave():
    while True: #Verificador da Palavra_Chave

        Palavra_chave = str(input('Palavra Chave: ').upper().strip()) #Recebe a palavra chave

        if string(Palavra_chave) == False: #Usa a função para verificar se palavra_chave é válida
            print("Valor INVÁLIDO")
        if string(Palavra_chave) == True:
            break
    return Palavra_chave


def Dicas(Palavra_chave):

    dicas = []  # lista para as dicas
    cont = 0  # contador das dicas
    while True:  # Validador dados Dicas

        dica = str(input(f'Dica {cont + 1}: ').upper().strip())
        if string(dica) == False:  # Valida a dica
            print("Valor INVÁLIDO")
        elif string(Palavra_chave) == True:  # Se for valida, adiciona a dica na lista e aumenta em +1 o cont
            dicas.append(dica)
            cont += 1
        if cont == 3:  # Significa que tem 3 dicas já, encerrando a solicitação de mais dicas
            break

    return dicas


def dados_arquivo():
    arquivo = open("rodadas.txt", "r")

    for linha in arquivo:
        print(linha)
    arquivo.close()