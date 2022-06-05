import os, time

def limpar():
    os.system("cls")

def esperar(segundos):
    time.sleep(segundos)

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
        if vez == 1:
            limpar()

        if resposta != "" and resposta != " ":
            respostas.append(resposta)
            vez = vez + 1

        elif resposta == "" or resposta == " ":
            limpar()
            print("Preencha corretamente")
            
    return respostas

def monta_oculta(oculta, palavra_chave):
    for posicao, letra in enumerate(palavra_chave):
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
        if dica == "" or dica == " ":
            limpar()
            print("Preencha corretamente")
        else:
            array_dicas.append(dica)
            vez = vez + 1
    return array_dicas

def escolha_usuario(vidas, palavra_oculta, dicas_pedidas):
    while True:
        try:
            escolha = int(input("Informe sua escolha: "))

            if escolha > 1 or escolha < 0:
                monta_tabuleiro(vidas, palavra_oculta, dicas_pedidas)
                print("Opção inválida")

            elif escolha == 1 and dicas_pedidas > 3:
                monta_tabuleiro(vidas, palavra_oculta, dicas_pedidas)
                print("Não possui mais dicas para consultar")

            else:
                return escolha
        except:
            monta_tabuleiro(vidas, palavra_oculta, dicas_pedidas)
            print("Opção inválida")

def registrar(informacoes):
    arquivo = open("Registro de partidas.txt","w")
    arquivo.write(informacoes)
    arquivo.close()

def ler_registro():
    arquivo = open("Registro de partidas.txt","r")
    conteudo = arquivo.readlines()
    arquivo.close()
    return conteudo

def armazenar(palavra, vencedor, perdedor):
    try:
        conteudo = ler_registro()
        conteudo.append("Palavra: %s - Vencedor: %s, Perdedor: %s\n"%(palavra, vencedor, perdedor))
        registrar(''.join(conteudo))
    except:
        conteudo = []
        conteudo.append("Palavra: %s - Vencedor: %s, Perdedor: %s\n"%(palavra, vencedor, perdedor))
        registrar(''.join(conteudo))

def escolha_jogo(vencedor, nome_vencedor, dados):
    while True:
        try:
            opcao_usuario = int(input("Informe sua escolha: "))

            if opcao_usuario < 0 or opcao_usuario > 1:
                mostrar_vitoria(vencedor, nome_vencedor, dados)
                print("Opção inválida")
            elif opcao_usuario != " ":
                return opcao_usuario
        except:
            mostrar_vitoria(vencedor, nome_vencedor, dados)
            print("Opção inválida")