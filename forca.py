import os, time
os.system("cls")

while True:
    nome_desafiante = input("Informe o nome do Desafiante: ")
    if nome_desafiante != "" and nome_desafiante != " ":
        break

while True:
    nome_competidor = input("Informe o nome do Competidor: ")
    if nome_competidor != "" and nome_competidor != " ":
        break

while True:
    os.system("cls")
    palavra_chave = input("Informe a palavra chave: ")
    if palavra_chave != "" and palavra_chave != " ":
        break

def monta_oculta(oculta):
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
            print("Preencha corretamente")
        else:
            array_dicas.append(dica)
            vez = vez + 1
    return array_dicas

palavra_oculta = monta_oculta("")
dicas = pede_dicas()
dicas_pedidas = 0
erros = 0
vidas = ["|", "|", "|", "|", "O"]

def monta_tabuleiro():
    os.system("cls")

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

def mostrar_vitoria(vencedor):
    os.system("cls")

    print(palavra_oculta)
    print("O %s ganhou\n"%vencedor)

    print(''.join(ler_registro()))
    print()

    print("Opções:")
    print("(0) Sair")
    print("(1) Nova Partida")

def escolha_usuario():
    while True:
        try:
            escolha = int(input("Informe sua escolha: "))

            if escolha > 1 or escolha < 0:
                monta_tabuleiro()
                print("Opção inválida")

            elif escolha == 1 and dicas_pedidas + 1 > 3:
                monta_tabuleiro()
                print("Não possui mais dicas para consultar")

            else:
                return escolha
        except:
            monta_tabuleiro()
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
        print(''.join(conteudo))
    except:
        conteudo = []
        conteudo.append("Palavra: %s - Vencedor: %s, Perdedor: %s\n"%(palavra, vencedor, perdedor))
        registrar(''.join(conteudo))
        print(''.join(conteudo))

def escolha_jogo(vencedor):
    while True:
        try:
            opcao_usuario = int(input("Informe sua escolha: "))

            if opcao_usuario < 0 or opcao_usuario > 1:
                mostrar_vitoria(vencedor)
                print("Opção inválida")
            elif opcao_usuario != " ":
                return opcao_usuario
        except:
            mostrar_vitoria(vencedor)
            print("Opção inválida")

while True:
    monta_tabuleiro()
    opcao_usuario = escolha_usuario()

    os.system("cls")
    if opcao_usuario == 1:
        print("Dica %d: %s"%(dicas_pedidas + 1, dicas[dicas_pedidas]))
        dicas_pedidas = dicas_pedidas + 1

    while True:
        print(palavra_oculta)
        jogada = input("Informe uma letra: ")
        if jogada != "" and jogada != " ":
            break
        
    errou = True
    nova_oculta = ""

    for posicao, letra in enumerate(palavra_chave):
        if letra.lower() != jogada.lower() and palavra_oculta[posicao] == "*":
            nova_oculta = nova_oculta + "*"

        elif jogada.lower() == letra.lower():
            nova_oculta = nova_oculta + letra
            errou = False
        
        elif letra == " ":
            nova_oculta = nova_oculta + " "
        else:
            nova_oculta = nova_oculta + letra

    palavra_oculta = nova_oculta
    
    if palavra_oculta.count("*") == 0:
        armazenar(palavra_chave, nome_competidor, nome_desafiante)
        mostrar_vitoria("Competidor")
        opcao_usuario = escolha_jogo("Competidor")
        if opcao_usuario == 0:
            break

        elif opcao_usuario == 1:
            os.system("cls")
            nome_desafiante = input("Informe o nome do Desafiante: ")
            nome_competidor = input("Informe o nome do Competidor: ")
            os.system("cls")
            palavra_chave = input("Informe a palavra chave: ")
            palavra_oculta = monta_oculta("")
            dicas = pede_dicas()
            dicas_pedidas = 0
            erros = 0
            vidas = ["|", "|", "|", "|", "O"]

    elif errou == True and (erros + 1) < 5:
        erros = erros + 1
        vidas[erros - 1] = " "
        os.system("cls")
        print("Erro: %d/5"%erros)
        time.sleep(2)
        
    elif (erros + 1) >= 5:
        armazenar(palavra_chave, nome_desafiante, nome_competidor)
        mostrar_vitoria("Desafiante")
        opcao_usuario = escolha_jogo("Desafiante")
        if opcao_usuario == 0:
            break

        elif opcao_usuario == 1:
            os.system("cls")
            nome_desafiante = input("Informe o nome do Desafiante: ")
            nome_competidor = input("Informe o nome do Competidor: ")
            os.system("cls")
            palavra_chave = input("Informe a palavra chave: ")
            palavra_oculta = monta_oculta("")
            dicas = pede_dicas()
            dicas_pedidas = 0
            erros = 0
            vidas = ["|", "|", "|", "|", "O"]