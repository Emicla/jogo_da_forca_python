from funcoes import limpar, esperar, pede_dados, monta_oculta, pede_dicas, monta_tabuleiro, mostrar_vitoria, escolha_usuario, armazenar, escolha_jogo

limpar()

perguntas_dados = ["Informe o nome do Desafiante: ", "Informe o nome do Competidor: ", "Informe a palavra chave: "]
dados = pede_dados(perguntas_dados)
palavra_oculta = monta_oculta("", dados[2])
dicas = pede_dicas()
dicas_pedidas = 0
erros = 0
vidas = ["|", "|", "|", "|", "O"]

while True:
    monta_tabuleiro(vidas, palavra_oculta, dicas_pedidas)
    opcao_usuario = escolha_usuario(vidas, palavra_oculta, dicas_pedidas)

    limpar()
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

    for posicao, letra in enumerate(dados[2]):
        if letra.lower() != jogada.lower() and palavra_oculta[posicao] == "*":
            nova_oculta = nova_oculta + "*"

        elif jogada.lower() == letra.lower() and palavra_oculta[posicao] == "*":
            nova_oculta = nova_oculta + letra
            errou = False
        
        elif letra == " ":
            nova_oculta = nova_oculta + " "
        else:
            nova_oculta = nova_oculta + letra

    palavra_oculta = nova_oculta
    ganhador = ["Competidor", dados[1], 0]

    if errou == True and erros < 5:
        erros = erros + 1
        vidas[erros - 1] = " "
        limpar()
        print("Erro: %d/5"%erros)
        esperar(2)
        
    elif erros >= 5:
        ganhador = ["Desafiante", dados[0], 1]

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