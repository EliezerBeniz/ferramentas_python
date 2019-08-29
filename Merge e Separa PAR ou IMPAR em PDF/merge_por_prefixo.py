####################################
# Autor:    Cleverson Vieira       #
#    cleverson.vieira@gmail.com    #
####################################

# Programa para arquivos em PDF.

# Pretende-se que:
# O programa cheque os ficheiros começados com determinado prefixo.
# Cheque os ficheiros para verificar se teen páginas pares.
    # Caso existea um ficheiro de páginas cuja contagem acuse ser impar o programa exibe uma Box com alerta e registra em ficheiro txt, como um tipo de log.
# Faça o merge dos tais ficheiros tranformando-os em apenas um, ficheiro.
# Logo a seguir ,serpare as paginas corespondentes a página da frente da página do verso.

# importando as bibliotecas nescessárias
import os
import PyPDF2
from tkinter import messagebox


#Aqui o sistema busca o prefixo que será informado em um conunto de ficheiros
# Vale resaltar que o program esta preparado para tratar somente ficheiros em PDF.

prefixo_ident = input('Qual prefixo de identificação do conjunto de ficheiros?:')

# Preparando algumas variáveis
file = os.listdir()
coletar_arquivos = PyPDF2.PdfFileMerger()
arquivos_erros = []
Erro = 0

# Aqui inicia ciclo de leitura da lista de ficheiros. 
for file in os.listdir():    
    # Aqui seleciona os ficheiros que iniciam com prefixo solicitado no começo do programa.
    if file.startswith(prefixo_ident):
        # Abertura e coleta de dados do ficheiro de cada ficheiro.
        with open(file,'rb') as f:
            pdf = PyPDF2.PdfFileReader(f)
            info = pdf.getDocumentInfo()
            n_Pag = pdf.getNumPages() #Será utilizado par verificar se é par ou impar.
            
            # Aqui é feita a verificação da piginção se é impar ou par.
            if n_Pag % 2 == 0:
                coletar_arquivos.append(file) # Se for par
            else: # se fro impar
                Erro = 1 # Altera o estado da váriavel Erro de 0 para 1
                messagebox.showwarning('Erro detetado!','Ficheiro com página Impar '+file+'\n Ficheiro com : '+str (n_Pag)+' - Páginas') # Dispara caixa de texto com alerta de erro, informando o nome do ficheiro e quantidade de página.
                arquivos_erros.append(file+'->'+str(n_Pag)+' - Páginas') # Armazena o erro na variável.
           
if Erro != 0:  # Se o estado da váriavel Erro foi alterado de 0 para 1 entrado IF.
    # Abre ou cria o ficheiro TXT, registra o erro e logo asseguir fecha o TXT.
    log_txt = open('LOG DE ERRO DE ARQUIVOS.TXT','w')
    log_txt.write(str(arquivos_erros))
    log_txt.close()
    
else:    
    # Caso não haja erro o sistema aqui vamos criar o ficheiro PDF já mesclado.       
    coletar_arquivos.write('merge_'+prefixo_ident+'_.pdf')
 #Fim    

 