from funcoes import limpar, esperar, pede_dados, monta_oculta, pede_dicas, monta_tabuleiro, mostrar_vitoria, opcoes_usuario, armazenar, escolha_jogo, remove_acento

limpar()

perguntas_dados = ["Informe o nome do Desafiante: ", "Informe o nome do Competidor: ", "Informe a palavra chave: "]
dicas_pedidas = 0
erros = 0
vidas = ["|", "|", "|", "|", "O"]

dados = pede_dados(perguntas_dados)
palavra_oculta = monta_oculta("", dados[2])
dicas = pede_dicas()

while True:
    monta_tabuleiro(vidas, palavra_oculta, dicas_pedidas)

    opcao_usuario = opcoes_usuario(vidas, palavra_oculta, dicas_pedidas, dicas)

    if opcao_usuario != "":
        dicas_pedidas = dicas_pedidas + 1
        
    limpar()

    while True:
        print(opcao_usuario)
        print(palavra_oculta)
        print()
        jogada = input("Informe uma letra: ")

        limpar()

        if len(jogada) > 1 and len(jogada) < len(dados[2]) or len(jogada) < 1 or len(jogada) > len(dados[2]):
            print("Preencha corretamente")

        elif jogada[0] == " ":
            print("Não use espaços em branco no ínicio da letra")

        else:
            break
        
    errou = True
    nova_oculta = ""
    ganhador = ["Competidor", dados[1], 0]
    palavra_sem_acento = remove_acento(dados[2])

    if jogada.lower() == dados[2].lower() or jogada.lower() == palavra_sem_acento.lower():
        nova_oculta = dados[2]

    else:
        for posicao, letra in enumerate(palavra_sem_acento):
            if letra.lower() != jogada.lower() and palavra_oculta[posicao] == "*":
                nova_oculta = nova_oculta + "*"

            elif jogada.lower() == letra.lower() and palavra_oculta[posicao] == "*":
                nova_oculta = nova_oculta + dados[2][posicao]
                errou = False
            
            elif letra == " ":
                nova_oculta = nova_oculta + " "
            else:
                nova_oculta = nova_oculta + dados[2][posicao]

        if errou == True and erros < 4:
            erros = erros + 1
            vidas[erros - 1] = " "
            limpar()
            print("Erro: %d/5"%erros)
            esperar(1)
            
        elif errou == True and erros >= 4:
            erros = erros + 1
            ganhador = ["Desafiante", dados[0], 1]

    palavra_oculta = nova_oculta

    if palavra_oculta.count("*") == 0 or erros >= 5:
        armazenar(dados[2], dados[-(ganhador[2]) + 1], dados[ganhador[2]])
        mostrar_vitoria(ganhador[0], ganhador[1], dados)
        opcao_usuario = escolha_jogo(ganhador[0], ganhador[1], dados)
        if opcao_usuario == 0:
            break

        elif opcao_usuario == 1:
            limpar()
            dados = pede_dados(perguntas_dados)
            palavra_oculta = monta_oculta("", dados[2])
            dicas = pede_dicas()
            dicas_pedidas = 0
            erros = 0
            vidas = ["|", "|", "|", "|", "O"]