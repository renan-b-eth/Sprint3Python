import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter import filedialog as fd
import os

# realizar a % de tempo que o usuario clica na tela e quantos clicks.
class Main():

    

    def ler_diretorio():
         # Cria uma janela Tk oculta para evitar a exibição da janela principal
        janela_padrao = Tk().withdraw()
        filename = fd.askopenfilename()

        # Obtém o diretório do arquivo selecionado
        diretorio = os.path.dirname(filename)

        # Obtém o nome do arquivo selecionado
        nome_arquivo = os.path.basename(filename)

        diretorio_completo = diretorio + "/" + nome_arquivo

        # Separando o diretório pelos '/'
        partes_do_diretorio = diretorio_completo.split('/')

        diretorio_correto = "./"+partes_do_diretorio[5]+"/"+partes_do_diretorio[6]+"/"+partes_do_diretorio[7]

        return diretorio_correto
    

    #pega o arquivo que eu selecionei.
    diretorio = ler_diretorio()
    df = pd.read_csv(diretorio)


    #def ler_csv():
        #df = pd.read_csv("./Sprint3Python/dados/click_data.csv")
        #return df
    
    def qtd_linhas(df):
        qtd_linhas = len(df)
        return qtd_linhas

    def qtd_clicks(df, qtd_clicks):
        i = 0
        qtd_header = 0
        qtd_main = 0
        qtd_footer = 0
        qtd_clicks_totais = {}
        while i < qtd_clicks:
            if(df["Y Position"].values[i] < 100):
                qtd_header = qtd_header + 1
                i = i+1
                #print("entrou aqui")
            elif((df["Y Position"].values[i] > 150) and (df["Y Position"].values[i] < 500)):
                qtd_main = qtd_main + 1
                i = i+1
            else:
                qtd_footer = qtd_footer + 1
                i = i+1
        qtd_clicks_totais = {'qtd_header': qtd_header,
            'qtd_main': qtd_main,
            'qtd_footer': qtd_footer
            } 
               
        
        return qtd_clicks_totais
    
    def porcentagem(df, qtd_clicks):
        qtd_total_clicks = qtd_clicks["qtd_header"] + qtd_clicks["qtd_main"] + qtd_clicks["qtd_footer"]
        porcentagem_total = 100
        porcentagem_header = (qtd_clicks["qtd_header"] * 100) / qtd_total_clicks
        porcentagem_main = (qtd_clicks["qtd_main"] * 100) / qtd_total_clicks
        porcentagem_footer = (qtd_clicks["qtd_footer"] * 100) / qtd_total_clicks
        
        porcentagens = {'por_header': round(porcentagem_header,2),
            'por_main': round(porcentagem_main,2),
            'por_footer': round(porcentagem_footer,2)
            } 

        return porcentagens
    
    
    clicks = qtd_clicks(df,60)

    ler_diretorio()
        
    print(qtd_clicks(df,60))
    print(porcentagem(df, clicks))

    



    

