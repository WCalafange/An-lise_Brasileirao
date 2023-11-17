#imports
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

#Ajuste de configuração de visualização de colunas
pd.set_option('max_columns', None)
pd.set_option('max_rows', None)

#Colunas que serão importadas
lista_colunas = ['Temporada',
                 'Série',
                 'Número do Jogo',
                 'Mandante',
                 'Gol Mandante',
                 'Gol Visitante',
                 'Visitante',
                 'Gols no Jogo',
                 'Resultado Mandante',
                 'Resultado Visitante']

#Tipos das Colunas
tipos_colunas = { 'Temporada': int,
                  'Série': str,
                  'Número do Jogo': int,
                  'Mandante': str,
                  'Gol Mandante': int,
                  'Gol Visitante': int,
                  'Visitante': str,
                  'Gols no Jogo': int,
                  'Resultado Mandante': str,
                  'Resultado Visitante': str }

#Importando o arquivo
df = pd.read_excel('CampeonatoBrasileiro_Jogos_CBF_20121017_SerieAB.xlsx',
                   usecols= lista_colunas,
                   dtype = tipos_colunas)

'''Listas utilizadas para salvar a quantidade de vitorias e empates
dos times da serie A. De modo que cada indíce é referente a uma 
temporada'''
numero_vitorias_casa_A = [0,0,0,0,0,0,0,0,0,0]
numero_vitorias_fora_A = [0,0,0,0,0,0,0,0,0,0]
numero_empates_A = [0,0,0,0,0,0,0,0,0,0]

'''Listas utilizadas para realizarem os calculos da porcentagem 
de vitórias e empates das partidas da série A. De modo que cada 
indíce é referente a uma temporada'''
porcentagem_vitorias_casa_A = [0,0,0,0,0,0,0,0,0,0]
porcentagem_vitorias_fora_A = [0,0,0,0,0,0,0,0,0,0]
porcentagem_empates_A = [0,0,0,0,0,0,0,0,0,0]
porcentagem_vitorias_casa_B = [0,0,0,0,0,0,0,0,0,0]
porcentagem_vitorias_fora_B = [0,0,0,0,0,0,0,0,0,0]
porcentagem_empates_B = [0,0,0,0,0,0,0,0,0,0]

'''Listas usadas para realizarem os calculos referentes aos mandantes
e o número de gols marcados. De modo que cada indice das listas faz 
referencia a quantidade de gols marcados pelas equipes mandantes'''
vitoria_casa_A = [0,0,0,0]
casa_naovenceu_A = [0,0,0,0]
chance_vitoria_casa_A = [0,0,0,0]

'''Listas usadas para realizarem os calculos referentes aos visitantes
e o número de gols marcado. De modo que cada indice das listas faz 
referencia a quantidade de gols marcados pelas equipes visitantes'''
vitoria_fora_A = [0,0,0,0,0]
empate_fora_A = [0,0,0,0,0]
derrota_fora = [0,0,0,0,0]
chance_vitoria_fora_A = [0,0,0,0,0]
chance_naoDerrota_fora_A = [0,0,0,0,0]

#Detarmina o vencedor da partida
def vencedor_partida(i, indice):
    if df.loc[i, 'Série'] == 'A':
        if df.loc[i, 'Gol Mandante'] > df.loc[i, 'Gol Visitante']:
            numero_vitorias_casa_A[indice] += 1
        elif df.loc[i, 'Gol Mandante'] < df.loc[i, 'Gol Visitante']:
            numero_vitorias_fora_A[indice] += 1
        else:
            numero_empates_A[indice] += 1

#Chama o método para determinar o vencedor da partida de acordo com a temporada em que a partida foi realizada
for i in range(len(df.index)):
    if df.loc[i,'Temporada'] == 2012:
        vencedor_partida(i,0)
    elif df.loc[i, 'Temporada'] == 2013:
        vencedor_partida(i,1)
    elif df.loc[i, 'Temporada'] == 2014:
        vencedor_partida(i,2)
    elif df.loc[i, 'Temporada'] == 2015:
        vencedor_partida(i,3)
    elif df.loc[i, 'Temporada'] == 2016:
        vencedor_partida(i,4)
    elif df.loc[i, 'Temporada'] == 2017:
        vencedor_partida(i,5)
    elif df.loc[i, 'Temporada'] == 2018:
        vencedor_partida(i,6)
    elif df.loc[i, 'Temporada'] == 2019:
        vencedor_partida(i,7)
    elif df.loc[i, 'Temporada'] == 2020:
        vencedor_partida(i,8)
    elif df.loc[i, 'Temporada'] == 2021:
        vencedor_partida(i,9)

#Transforma o número geral de partidas ganhas e empatadas em porcentagem
for p in range(len(numero_vitorias_casa_A)):
    porcentagem_vitorias_casa_A[p] = (numero_vitorias_casa_A[p]*100)/380
    porcentagem_vitorias_fora_A[p] = (numero_vitorias_fora_A[p]*100)/380
    porcentagem_empates_A[p] = (numero_empates_A[p]*100)/380

#Determina a quantidade de partidas em que o time mandante venceu ou não venceu a partida de acordo com a quantidade de gols marcada
def calculo_vitorias_casa():
    for v in range(len(df.index)):
        if df.loc[v,'Série'] == 'A':

            if df.loc[v,'Gol Mandante'] == 1:
                if df.loc[v,'Resultado Mandante'] == 'Vitoria':
                    vitoria_casa_A[0] += 1
                else:
                    casa_naovenceu_A[0] += 1

            elif df.loc[v,'Gol Mandante'] == 2:
                if df.loc[v,'Resultado Mandante'] == 'Vitoria':
                    vitoria_casa_A[1] += 1
                else:
                    casa_naovenceu_A[1] += 1

            elif df.loc[v, 'Gol Mandante'] == 3:
                if df.loc[v, 'Resultado Mandante'] == 'Vitoria':
                    vitoria_casa_A[2] += 1
                else:
                    casa_naovenceu_A[2] += 1

            elif df.loc[v, 'Gol Mandante'] >= 4:
                if df.loc[v, 'Resultado Mandante'] == 'Vitoria':
                    vitoria_casa_A[3] += 1
                else:
                    casa_naovenceu_A[3] += 1

#Determina a quantidade de vitórias, empates e derrotas do time visitante de acordo com a quantidade de gols marcada
def calculo_vitorias_fora():
    for m in range(len(df.index)):
        if df.loc[m,'Série'] == 'A':

            if df.loc[m,'Gol Visitante'] == 1:
                if df.loc[m,'Resultado Visitante'] == 'Vitoria':
                    vitoria_fora_A[1] += 1
                elif df.loc[m,"Resultado Visitante"] == "Empate":
                    empate_fora_A[1] += 1
                else:
                    derrota_fora[1] += 1

            elif df.loc[m, 'Gol Visitante'] == 2:
                if df.loc[m, 'Resultado Visitante'] == 'Vitoria':
                    vitoria_fora_A[2] += 1
                elif df.loc[m, "Resultado Visitante"] == "Empate":
                    empate_fora_A[2] += 1
                else:
                    derrota_fora[2] += 1

            elif df.loc[m, 'Gol Visitante'] == 3:
                if df.loc[m, 'Resultado Visitante'] == 'Vitoria':
                    vitoria_fora_A[3] += 1
                elif df.loc[m, "Resultado Visitante"] == "Empate":
                    empate_fora_A[3] += 1
                else:
                    derrota_fora[3] += 1

            elif df.loc[m, 'Gol Visitante'] >= 4:
                if df.loc[m, 'Resultado Visitante'] == 'Vitoria':
                    vitoria_fora_A[4] += 1
                elif df.loc[m, "Resultado Visitante"] == "Empate":
                    empate_fora_A[4] += 1
                else:
                    derrota_fora[4] += 1

            elif df.loc[m,'Gol Visitante'] == 0:
                if df.loc[m, 'Resultado Visitante'] == 'Empate':
                    empate_fora_A[0] += 1
                else:
                    derrota_fora[0] += 1

#Calcula as porcentagens do time mandante vencer a partida
def probabilidade_vitoria_casa():
    for q in range(len(vitoria_casa_A)):
        chance_vitoria_casa_A[q] = (vitoria_casa_A[q]*100)/(vitoria_casa_A[q]+casa_naovenceu_A[q])

#Calcula as porcentagens do time visitante vencer a partida
def probabilidade_vitoria_fora():
    for r in range(len(vitoria_fora_A)):
        chance_vitoria_fora_A[r] = (vitoria_fora_A[r]*100)/(vitoria_fora_A[r]+empate_fora_A[r]+derrota_fora[r])

#Calcula as porcentagens do time visitante não perder o jogo
def probabilidade_naoderrota_fora():
    for t in range(len(vitoria_fora_A)):
        chance_naoDerrota_fora_A[t] = ((vitoria_fora_A[t] + empate_fora_A[t])*100)/(vitoria_fora_A[t]+empate_fora_A[t]+derrota_fora[t])

#Constroi o grafico de porcentagem de vitorias
def grafico_vitorias():
    # Gráfico de Barras para porcentagem de vitórias
    barWidth = 0.25  # largura do gráfico
    plt.figure(figsize=(12, 7))  # tamanho do gráfico
    # Posição das barras
    r1 = np.arange(len(numero_vitorias_casa_A))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    # Criando as barras
    plt.bar(r1, porcentagem_vitorias_casa_A, color='green', width=barWidth, label='Vitórias Casa')
    plt.bar(r2, porcentagem_empates_A, color='yellow', width=barWidth, label='Empates')
    plt.bar(r3, porcentagem_vitorias_fora_A, color='blue', width=barWidth, label='Vitórias Fora')

    # Adicionando Legendas as barras
    plt.xlabel('Ano')
    plt.xticks([r + barWidth for r in range(len(numero_vitorias_casa_A))],
               ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'])
    plt.ylabel('Porcentagem do número de vitórias')
    plt.title('Representação de vitórias dos times da série A entre 2012 e 2021')
    plt.legend()
    plt.show()

#Constroi o gráfico com as probabilidades de vitorias do time mandante de acordo com a quantidade de gols marcada
def grafico_probalidade_vitoria():
    quantidade_gols = ['1','2','3','4 ou mais gols']

    plt.bar(quantidade_gols, chance_vitoria_casa_A, color='blue')

    plt.xticks(quantidade_gols)
    plt.ylabel('Porcentagem de vitórias')
    plt.xlabel('Quantidade de gols')
    plt.title('Porcentagem vitórias do time mandante da série A pela quantidade de gols marcada')

    plt.show()

#Constroi o gráfico com as probabilidades de vitorias do time visitante de acordo com a quantidade de gols marcada
def grafico_probabilidade_vitoria_fora():
    quantidade_gols = ['0', '1', '2', '3', '4 ou mais gols']

    plt.bar(quantidade_gols, chance_vitoria_fora_A, color='blue')

    plt.xticks(quantidade_gols)
    plt.ylabel('Porcentagem de vitórias')
    plt.xlabel('Quantidade de gols')
    plt.title('Porcentagem de vitórias do time visitante da série A pela quantidade de gols marcada')

    plt.show()

#Constroi o gráfico com as probabilidades do time visitante não perder o jogo  de acordo com a quantidade de gols marcada
def grafico_probabilidade_naoDerrota_fora():
    quantidade_gols = ['0', '1', '2', '3', '4 ou mais gols']

    plt.bar(quantidade_gols, chance_naoDerrota_fora_A, color='blue')

    plt.xticks(quantidade_gols)
    plt.ylabel('Porcentagem de partidas não perdidas')
    plt.xlabel('Quantidade de gols')
    plt.title('Porcentagem de partidas que o time visitante não perdeu na série A pela quantidade de gols marcada')

    plt.show()

calculo_vitorias_casa()
probabilidade_vitoria_casa()
calculo_vitorias_fora()
probabilidade_vitoria_fora()
probabilidade_naoderrota_fora()
grafico_vitorias()
grafico_probalidade_vitoria()
grafico_probabilidade_vitoria_fora()
grafico_probabilidade_naoDerrota_fora()


