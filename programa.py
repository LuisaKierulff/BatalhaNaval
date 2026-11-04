
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
print(frota)