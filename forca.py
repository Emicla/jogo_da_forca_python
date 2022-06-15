from funcoes_jogo import limpar, pede_dados, monta_oculta, pede_dicas, monta_tabuleiro, opcoes_usuario, armazenar, escolha_jogo, verifica_letra, verifica_errou
from funcoes_gerais import remove_acento

perguntas = ["Informe o nome do Desafiante: ", "Informe o nome do Competidor: ", "Informe a palavra chave: "]

def jogo():
    limpar()

    dicas_pedidas = 0
    erros = 0
    vidas = ["|", "|", "|", "|", "O"]

    dados = pede_dados(perguntas)
    palavra_oculta = monta_oculta("", dados[2])
    dicas = pede_dicas()
    palavra_sem_acento = remove_acento(dados[2])

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

        array_vericou_letra = verifica_letra(jogada, palavra_oculta, dados[2], palavra_sem_acento)
        array_de_errou = verifica_errou(array_vericou_letra[0], erros, dados[0], dados[1], vidas)

        erros = array_de_errou[1]
        vidas = array_de_errou[2]
        ganhador = array_de_errou[0]
        palavra_oculta = array_vericou_letra[1]

        if palavra_oculta.count("*") == 0 or erros >= 5:
            armazenar(dados[2], dados[-(ganhador[2]) + 1], dados[ganhador[2]])
            opcao_usuario = escolha_jogo(ganhador[0], ganhador[1], dados)
            return opcao_usuario

while True:
    if jogo() == 0:
        break