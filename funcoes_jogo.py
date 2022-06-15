from funcoes_gerais import limpar, esperar

def monta_tabuleiro(vidas, palavra_oculta, dicas_pedidas):
    limpar()

    print(" --------")
    print("|       |")
    print("|       {0}".format(vidas[4]))
    print("|       {0}".format(vidas[3]))
    print("|       {0}".format(vidas[2]))
    print("|      {0} {1}".format(vidas[1], vidas[0]))
    print("|")
    print("| ",palavra_oculta)
    print(" ")
    print(" (0) Jogar")
    if dicas_pedidas + 1 <= 3:
        print(" (1) Solicitar Dica (%d/3)"%(dicas_pedidas))
    print("")

def mostrar_vitoria(vencedor, nome_vencedor, dados):
    limpar()

    print("A palavra é: ",dados[2])
    print("O %s %s ganhou\n"%(vencedor, nome_vencedor))

    print("Histórico:")
    print()
    print(''.join(ler_registro()))
    print()

    print("Opções:")
    print("(0) Sair")
    print("(1) Nova Partida")

def pede_dados(perguntas):
    respostas = []
    vez = 0
    while vez < len(perguntas):
        resposta = input(perguntas[vez])
        try:
            resposta = int(resposta)
            limpar()
            print("Não pode ter números")
            continue
        except:
            if vez == 1:
                limpar()

            if len(resposta) < 2:
                limpar()
                print("Deve ter 2 ou mais letras")

            elif resposta[0] == " " or resposta[1] == " ":
                limpar()
                print("Deve ter mais de 2 letras o primeiro nome e sem espaços na frente")

            else:
                respostas.append(resposta)
                vez = vez + 1 
    return respostas

def monta_oculta(oculta, palavra_chave):
    for letra in palavra_chave:
        if letra == " ":
            oculta = oculta + " "
        else:
            oculta = oculta + "*"
    return oculta

def pede_dicas():
    array_dicas = []
    vez = 1
    while vez < 4:
        dica = input("Informe a Dica %d: "%vez)
        if len(dica) == 0:
            limpar()
            print("Preencha corretamente")

        elif dica[0] == " ":
            limpar()
            print("Não pode ter espaços antes da dica")

        else:
            array_dicas.append(dica)
            vez = vez + 1
    return array_dicas

def opcoes_usuario(vidas, palavra_oculta, dicas_pedidas, dicas):
    while True:
        try:
            escolha = int(input("Informe sua escolha: "))

            if escolha > 1 or escolha < 0:
                monta_tabuleiro(vidas, palavra_oculta, dicas_pedidas)
                print("Opção inválida")

            elif escolha == 1 and dicas_pedidas >= 3:
                monta_tabuleiro(vidas, palavra_oculta, dicas_pedidas)
                print("Não possui mais dicas para consultar")

            elif escolha == 1:
                return "Dica %d: %s"%(dicas_pedidas + 1, dicas[dicas_pedidas])
            else:
                return ""
        except:
            monta_tabuleiro(vidas, palavra_oculta, dicas_pedidas)
            print("Opção inválida")

def verifica_letra(letra_jogada, palavra_oculta, palavra_chave, palavra_sem_acento):
    errou = True
    nova_oculta = ""

    if letra_jogada.lower() == palavra_chave.lower() or letra_jogada.lower() == palavra_sem_acento.lower():
        nova_oculta = palavra_chave

    else:
        for posicao, letra in enumerate(palavra_sem_acento):
            if letra.lower() != letra_jogada.lower() and palavra_oculta[posicao] == "*":
                nova_oculta = nova_oculta + "*"

            elif letra_jogada.lower() == letra.lower() and palavra_oculta[posicao] == "*":
                nova_oculta = nova_oculta + palavra_chave[posicao]
                errou = False
                
            elif letra == " ":
                nova_oculta = nova_oculta + " "
            else:
                nova_oculta = nova_oculta + palavra_chave[posicao]

    return [errou, nova_oculta]

def verifica_errou(se_errou, quantidade_erros, desafiante, competidor, vidas):

    ganhador = ["Competidor", competidor, 0]

    if se_errou == True and quantidade_erros < 4:
        quantidade_erros = quantidade_erros + 1
        vidas[quantidade_erros - 1] = " "
        limpar()
        print("Erro: %d/5"%quantidade_erros)
        esperar(1)
                
    elif se_errou == True and quantidade_erros >= 4:
        quantidade_erros = quantidade_erros + 1
        ganhador = ["Desafiante", desafiante, 1]
    
    return [ganhador, quantidade_erros, vidas]


def registrar(informacoes):
    arquivo = open("Registro de partidas.txt", "w")
    arquivo.write(informacoes)
    arquivo.close()

def ler_registro():
    arquivo = open("Registro de partidas.txt", "r")
    conteudo = arquivo.readlines()
    arquivo.close()
    return conteudo

def armazenar(palavra, vencedor, perdedor):
    try:
        conteudo = ler_registro()
    except:
        conteudo = []
        
    conteudo.append("Palavra: %s - Vencedor: %s, Perdedor: %s\n"%(palavra, vencedor, perdedor))
    registrar(''.join(conteudo))

def escolha_jogo(vencedor, nome_vencedor, dados):
    mostrar_vitoria(vencedor, nome_vencedor, dados)
    while True:
        try:
            opcao_usuario = int(input("Informe sua escolha: "))

            if opcao_usuario < 0 or opcao_usuario > 1:
                mostrar_vitoria(vencedor, nome_vencedor, dados)
                print("Opção inválida")

            else:
                return opcao_usuario
        except:
            mostrar_vitoria(vencedor, nome_vencedor, dados)
            print("Opção inválida")