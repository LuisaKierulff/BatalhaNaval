# BatalhaNaval
#Projeto de Batalha Naval desenvolvido em dupla
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