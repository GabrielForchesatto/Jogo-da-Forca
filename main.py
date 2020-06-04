from functions import string, linha, asteriscos, Competidor, Desafiante, Palavra_chave, Dicas, dados_arquivo
import os 

#Arquivo = open("rodadas.txt", "a")
os.system('cls')
while True:
    Arquivo = open("rodadas.txt", "a")
    desafiante = Desafiante()
    competidor = Competidor()
    os.system('cls')
    linha()
    print(f'Vez de {desafiante.upper()} jogar')
    linha()

    palavra_chave = Palavra_chave()
    Arquivo.write(f'Palavra: {palavra_chave} - ')

    dicas = Dicas(palavra_chave)

    cont_dica = 0
    erros = 0
    letras_digitadas = []
    letras_acertadas = []
    print('Palavra: ', end = '')
    asteriscos(palavra_chave)
    os.system('cls')
    while True:

        senha = ''
        while True:

            linha()
            
            opcao = str(input('Jogar ou dica? ').upper().strip())
            if opcao != "JOGAR" and opcao != "DICA":
                print('Opção INVÁLIDA')
            if opcao == "JOGAR" or opcao == "DICA":
                linha()
                break

        if opcao == "JOGAR":

            if letras_digitadas == []:
                print('Palavra: ', end = '')
                asteriscos(palavra_chave)

            while True:
                tentativa = str(input("Digite uma letra: ").upper().strip())
                if string(tentativa) == False or len(tentativa) > 1:
                    print("Valor INVÁLIDO")
                if string(tentativa) == True and len(tentativa) == 1:
                    break

            if tentativa in letras_digitadas:
                print("Letra já informada!")

            else:
                letras_digitadas += tentativa
                if tentativa in palavra_chave:
                    letras_acertadas += tentativa
                else:
                    erros += 1
                    print("Letra ERRADA")
                    print(f'Erros: {erros}')
            for letra in palavra_chave:

                if letra in letras_acertadas:
                    senha += letra
                else:
                    senha += "*"

            if senha == palavra_chave:
                print("Resposta correta!")
                print(f'Palavra: {senha}')
                print(f'O {competidor} GANHOU!!')
                Arquivo.write(f'Vencedor: {competidor}, Desafiante: {desafiante}\n')
                break
            print(f'Palavra: {senha}')

        if cont_dica == 3:
            print('Acabou as dicas')
            linha()
        else:

            if opcao == 'DICA':

                print(f'Dica: {dicas[cont_dica]}')
                linha()
                cont_dica +=1

                if letras_digitadas == []:
                    print(f'Palavra: ', end = '')
                    asteriscos(palavra_chave)

                while True:
                    tentativa = str(input("Digite uma letra: ").upper().strip())
                    if string(tentativa) == False or len(tentativa) > 1:
                        print("Valor INVÁLIDO")
                    if string(tentativa) == True and len(tentativa) == 1:
                        break

                if tentativa in letras_digitadas:
                    print("Letra já informada!")

                else:
                    letras_digitadas += tentativa
                    if tentativa in palavra_chave:
                        letras_acertadas += tentativa
                    else:
                        erros += 1
                        print("Letra ERRADA")
                        print(f'Erros: {erros}')
                for letra in palavra_chave:

                    if letra in letras_acertadas:
                        senha += letra
                    else:
                        senha += "*"

                if senha == palavra_chave:

                    print("Resposta correta!")
                    print(f'Palavra: {senha}')
                    print(f'O {competidor} GANHOU!!!')
                    Arquivo.write(f'Vencedor: {competidor}, Desafiante: {desafiante}\n')

                    break

                print(f'Palavra: {senha}')

            if erros == 6: #caso o usuário erre 6 vezes, o programa é encerrado
                linha()
                print(f'ACABOU AS TENTATIVAS, O {desafiante} GANHOU!')
                Arquivo.write(f'Perdedor: {competidor}, Desafiante: {desafiante} \n')
                break

    Arquivo.close()  # Fecha o .txt
    continuar = str(input('Continuar [S/N]: ').upper().strip())
    linha()
    if continuar == 'N':
        dados_arquivo()
        print("Obrigado por jogar")

        break
    if continuar == 'S':
        dados_arquivo()  # Função que abre o .txt no modo Read e mostra as linhas em ordem
        linha()