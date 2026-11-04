# BatalhaNaval
#Projeto de Batalha Naval desenvolvido em dupla
#exercício 1
def define_posicoes (linha,coluna,orientecao,tamanho):
    lista=[]
    if orientecao=='vertical':
        i=0 
        while i < tamanho:
            lista.append([linha+i, coluna])
            i+=1
    if orientecao== 'horizontal':
        i=0
        while i < tamanho:
            lista.append([linha, coluna+i])
            i+=1
    return lista



#print (define_posicoes(2,4,'vertical',3))

#exercício 2
def preenche_frota (frota,nome_navio,linha, coluna, orientacao, tamanho ):
    lista= define_posicoes(linha,coluna,orientacao, tamanho)
    resultado=frota
    if nome_navio not in frota:
        resultado[nome_navio]=[lista]
    else:
        resultado[nome_navio].append(lista)
    return resultado



#exercicio 3 
def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X" 
    else: 
        tabuleiro[linha][coluna] = "-" 
    return tabuleiro


#exercício 4 
def posiciona_frota (dicionario):
    lista= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for l in dicionario.values():
        i=0
        while i < len(l):
            j=0
            while j< len (l[i]):
                lista[l[i][j][0]][l[i][j][1]] = 1
                j+=1    
            i+=1
    return lista

#exercico 5
def afundados (dicionario,tabuleiro):
    afundados=0
    for l in dicionario.values():
        i=0
        while i < len(l):
                j=0
                c=0
                while j< len (l[i]):
                    if tabuleiro[l[i][j][0]][l[i][j][1]]== 'X':
                        c+=1
                    j+=1
                if c==j:
                    afundados+=1
                i+=1
    return afundados

#exercicio 6 
def posicao_valida (dicionario,linha,coluna,orientacao,tamanho):
    lista= define_posicoes (linha,coluna,orientacao,tamanho)
    i=0
    while i<len(lista):
        for posicoes in dicionario.values():
            for c in posicoes:
                if lista[i] in c:
                    return False
        if lista[i][0]>9 or lista[i][1]>9 or lista[i][1]<0 or lista[i][0]<0:
            return False
        i+=1
    return True



        
    
        



