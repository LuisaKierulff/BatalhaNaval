
from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida

#exercicio 7
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
for tipo in frota.keys():
    if tipo == "porta-aviões":
        tamanho = 4
        quantidade = 1
    if tipo == "navio-tanque":
        tamanho = 3
        quantidade = 2
    if tipo == "contratorpedeiro":
        tamanho = 2
        quantidade = 3
    if tipo == "submarino":
        tamanho = 1
        quantidade = 4
    i = 0
    while i < quantidade:
        valida = False
        while valida == False:
            print("Insira as informações referentes ao navio", tipo, "que possui tamanho", tamanho)
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
            if tipo != "submarino":
                o = int(input("1 ou 2"))
                if o == 1:
                    o = "vertical"
                if o == 2:
                    o = "horizontal"
            if tipo == "submarino":
                o = "horizontal"
            valida = posicao_valida(frota, l, c, o, tamanho)
            if valida == False:
                print("Esta posição não está válida!")
            if valida == True:
                preenche_frota(frota, tipo, l, c, o, tamanho)
        i += 1

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_inimigo= posiciona_frota(frota_oponente)
tabuleiro= posiciona_frota(frota)


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


tabuleiro_jogo= monta_tabuleiros(tabuleiro,tabuleiro_inimigo)
print(tabuleiro_jogo)
historico_jogadas=[]
jogando=True
while jogando==True:
    

    linha_jogada= int(input('linha'))
    while linha_jogada not in [0,1,2,3,4,5,6,7,8,9]:
        print('Linha inválida!')
        linha_jogada= int(input('linha'))


    coluna_jogada=int(input('coluna'))
    while coluna_jogada not in [0,1,2,3,4,5,6,7,8,9]:
        print('Coluna inválida!')
        coluna_jogada=int(input('coluna'))

    jogada=[linha_jogada,coluna_jogada]
    
    
    if jogada in historico_jogadas:
        print(f'A posição linha {linha_jogada} e coluna {coluna_jogada} já foi informada anteriormente!')
    else:
        historico_jogadas.append(jogada)
        tabuleiro_inimigo= faz_jogada(tabuleiro_inimigo,jogada[0],jogada[1])
        if afundados(frota_oponente,tabuleiro_inimigo)== 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando=False
        if jogando==True:
            tabuleiro_jogo= monta_tabuleiros(tabuleiro,tabuleiro_inimigo)
            print(tabuleiro_jogo)       





