from tkinter import *
from tkinter import ttk
from modules.dic_regiao_cidade import regiao_cidades
from modules.functions import *

cor1 = '#1a1918'  # preto
cor4 = "#ECEFF1"  # cinza
cor6 = '#E5BF2E'  #amarelo
cor7 = '#262424'  #PRETO
cor8 = '#FF0000'  #vermelho

janela = Tk()
janela.title("Calculadora de Frete")
janela.geometry("320x490")
janela.config(bg=cor4)


image = PhotoImage(file="assets/logo-copobras-2.png")

label = Label(janela, image=image).pack()



# label para a pergunta da cidade
lbl_cidade = Label(janela, text="Qual a cidade do destino?", font=("Arial 12 bold"), bg=cor6, fg=cor1)
lbl_cidade.pack(pady=5)

# entry para a cidade
ent_cidade = Entry(janela, font=("Arial 12 bold"), width =30, justify = CENTER, bg=cor4, fg=cor1)
ent_cidade.pack(pady=8)

# label para a pergunta da cubagem
lbl_cubagem = Label(janela, text="Qual o volume? (m\u00b3)", font=("Arial 12 bold"), bg=cor6, fg=cor1)
lbl_cubagem.pack(pady=5)

# entry para a cubagem
ent_cubagem = Entry(janela, font=("Arial 12 bold"), width =10, justify = CENTER,bg=cor4, fg=cor1)
ent_cubagem.pack(pady=8)

aviso = StringVar()
lbl_aviso = Label(janela, textvariable=aviso,  width =60,  justify = CENTER, font=("Arial 11 bold"), bg=cor4, fg=cor8)
lbl_aviso.pack(pady=2)

resultado = StringVar()
lbl_resultado = Label(janela, textvariable=resultado, font=("Arial 12 bold"), width =30, justify = CENTER, bg=cor4, fg=cor1)
lbl_resultado.pack(pady=4)

valor_fixo = StringVar()
lbl_valor_fixo = Label(janela, textvariable=valor_fixo, font=("Arial 12 bold"), width =30, justify = CENTER, bg=cor4, fg=cor1)
lbl_valor_fixo.pack(pady=4)

def calcular():
    cidade = ent_cidade.get().upper()
    cubagem = float(ent_cubagem.get().replace(',', '.'))
    regiao = ''

    cidade_encontrada = False
    for chave in regiao_cidades:
        if cidade in regiao_cidades[chave]:
            regiao = str(chave)
            cidade_encontrada = True
            break

    if not cidade_encontrada:
        resultado.set('')
        valor_fixo.set('')
        aviso.set('Cidade não encontrada. \n ENTRE EM CONTATO COM A LOGÍSTICA')

    while cidade_encontrada:
        if regiao == 'ALTO CAPIBARIBE':
            valor_frete, valor_constante = function_1(cubagem)
        elif regiao == 'ARARIPINA':
            valor_frete, valor_constante = function_2(cubagem)
        elif regiao == 'BREJO PERNAMBUCANO':
            valor_frete, valor_constante = function_3(cubagem)
        elif regiao == 'GARANHUNS' or regiao == 'ITAPARICA' or regiao == 'MATA MERIDIONAL PERNAMBUCANA' or regiao == 'MATA SETENTRIONAL PERNAMBUCANA' or regiao == 'MEDIO CAPIBARIBE':
            valor_frete, valor_constante = function_4(cubagem)
        elif regiao == 'ITAMARACA' or regiao == 'SUAPE':
            valor_frete, valor_constante = function_5(cubagem)
        elif regiao == 'PAJEU':
            valor_frete, valor_constante = function_6(cubagem)
        elif regiao == 'PETROLINA':
            valor_frete, valor_constante = function_7(cubagem)
        
        elif regiao == 'RECIFE' or regiao == 'VITORIA DE SANTO ANTAO':
            valor_frete, valor_constante = function_8(cubagem)

        elif regiao == 'SALGUEIRO' or regiao == 'SERTAO DO MOXOTO':
            valor_frete, valor_constante = function_9(cubagem)

        elif regiao == 'VALE DO IPANEMA' or regiao == 'VALE DO IPOJUCA':
            valor_frete, valor_constante = function_10(cubagem)

        aviso.set('')
        valor_fixo.set(f'Valor tabelado do m\u00b3 : {valor_constante}')
        resultado.set(f"Valor do frete: R$ {valor_frete:.2f}")
        break

btn_calcular = Button(janela, text="Calcular", command=calcular,width=10, height=2, bg=cor6, fg=cor1,  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
btn_calcular.pack(pady=5)

janela.mainloop()
