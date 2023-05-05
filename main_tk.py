from tkinter import *

janela = Tk()

# label para a pergunta da cidade
lbl_cidade = Label(janela, text="Qual a cidade do destino?")
lbl_cidade.pack()

# entry para a cidade
ent_cidade = Entry(janela)
ent_cidade.pack()

# label para a pergunta da cubagem
lbl_cubagem = Label(janela, text="Qual o volume? (metros cúbicos)")
lbl_cubagem.pack()

# entry para a cubagem
ent_cubagem = Entry(janela)
ent_cubagem.pack()


resultado = StringVar()

lbl_resultado = Label(janela, textvariable=resultado)
lbl_resultado.pack()

aviso = StringVar()
lbl_aviso = Label(janela, textvariable=aviso)
lbl_aviso.pack()

def calcular():
    cidade = ent_cidade.get().upper()
    cubagem = float(ent_cubagem.get().replace(',', '.'))
    regiao =''
    regiao_cidades = {'ALTO CAPIBARIBE':['CASINHAS', 'FREI MIGUELINHO', 'SANTA CRUZ DO CAPIBARIBE', 'SANTA MARIA DO CAMBUCA', 
    'SURUBIM', 'TAQUARITINGA DO NORTE', 'TORITAMA', 'VERTENTE DO LERIO', 'VERTENTES'], 'ARARIPINA': ['ARARIPINA', 'BODOCO', 'EXU', 'GRANITO',
    'IPUBI', 'MOREILANDIA', 'OURICURI', 'SANTA CRUZ', 'SANTA FILOMENA', 'TRINDADE'], 'BREJO PERNAMBUCANO': ['AGRESTINA', 'ALTINHO', 'BARRA DE GUABIRABA', 
    'BONITO', 'CAMOCIM DE SAO FELIX', 'CUPIRA', 'IBIRAJUBA', 'LAGOA DOS GATOS', 'PANELAS', 'SAIRE', 'SAO JOAQUIM DO MONTE'],' GARANHUNS': ['ANGELIM', 'BOM CONSELHO', 
    'BREJAO', 'CAETES', 'CALCADO', 'CANHOTINHO', 'CORRENTES', 'GARANHUNS', 'IATI', 'JUCATI', 'JUPI', 'JUREMA', 'LAGOA DO OURO', 'LAJEDO', 'PALMEIRINA', 'PARANATAMA',
    'SALOA', 'SAO JOAO', 'TEREZINHA'], 'ITAMARACA': ['ARACOIABA', 'IGARASSU','ILHA DE ITAMARACA', 'ITAMARACA', 'ITAPISSUMA'], 'ITAPARICA': ['BELEM DE SAO FRANCISCO',
    'CARNAUBEIRA DA PENHA', 'FLORESTA', 'ITACURUBA', 'JATOBA', 'PETROLANDIA', 'TACARATU'], 'MATA MERIDIONAL PERNAMBUCANA': ['AGUA PRETA', 'AMARAJI', 'BARREIROS', 
    'BELEM DE MARIA', 'CATENDE', 'CORTES', 'ESCADA', 'GAMELEIRA', 'JAQUEIRA', 'JOAQUIM NABUCO', 'MARAIAL', 'PALMARES', 'PRIMAVERA','QUIPAPA',
    'RIBEIRAO', 'RIO FORMOSO', 'SAO BENEDITO DO SUL', 'SAO JOSE DA COROA GRANDE', 'SIRINHAEM', 'TAMANDARE', 'XEXEU'],'MATA SETENTRIONAL PERNAMBUCANA':['ALIANCA', 
    'BUENOS AIRES', 'CAMUTANGA', 'CARPINA', 'CONDADO', 'FERREIROS', 'GOIANA', 'ITAMBE', 'ITAQUITINGA', 'LAGOA DO CARRO', 'LAGOA DO ITAENGA', 'MACAPARANA', 'NAZARE DA MATA',
    'PAUDALHO', 'TIMBAUBA', 'TRACUNHAEM', 'VICENCIA'],'MEDIO CAPIBARIBE':['BOM JARDIM', 'CUMARU', 'FEIRA NOVA', 'JOAO ALFREDO', 'LIMOEIRO', 'MACHADOS', 'OROBO', 'PASSIRA', 
    'SALGADINHO', 'SAO VICENTE FERRER'],'PAJEU':['AFOGADOS DA INGAZEIRA', 'BREJINHO', 'CALUMBI', 'CARNAIBA', 'FLORES', 'IGUARACI', 'INGAZEIRA', 'ITAPETIM', 'QUIXABA', 
    'SANTA CRUZ DA BAIXA VERDE', 'SANTA TEREZINHA', 'SAO JOSE DO EGITO', 'SERRA TALHADA', 'SOLIDAO', 'TABIRA', 'TRIUNFO', 'TUPARETAMA'],'PETROLINA':['AFRANIO', 'CABROBO', 'DORMENTES',
    'LAGOA GRANDE', 'OROCO', 'PETROLINA', 'SANTA MARIA DA BOA VISTA', 'TERRA NOVA'], 'RECIFE':['ABREU E LIMA', 'CAMARAGIBE', 'JABOATAO DOS GUARARAPES', 'MORENO', 'OLINDA', 'PAULISTA', 'RECIFE', 'SAO LOURENCO DA MATA'],
    'SALGUEIRO':['CEDRO', 'MIRANDIBA', 'PARNAMIRIM', 'SALGUEIRO', 'SAO JOSE DO BELMONTE', 'SERRITA', 'VERDEJANTE'], 'SERTAO DO MOXOTO':['ARCOVERDE', 'BETANIA', 'CUSTODIA', 'IBIMIRIM',
    'INAJA', 'MANARI', 'SERTANIA'], 'SUAPE':['CABO DE SANTO AGOSTINHO', 'IPOJUCA'], 'VALE DO IPANEMA':['AGUAS BELAS', 'BUIQUE', 'ITAIBA', 'PEDRA', 'TUPANATINGA', 'VENTUROSA'],
    'VALE DO IPOJUCA':['ALAGOINHA', 'BELO JARDIM', 'BEZERROS', 'BREJO DA MADRE DE DEUS', 'CACHOEIRINHA', 'CAPOEIRAS', 'CARUARU', 'GRAVATA', 'JATAUBA', 'PESQUEIRA', 'POCAO', 
    'RIACHO DAS ALMAS', 'SANHARO', 'SAO BENTO DO UNA', 'SAO CAITANO', 'TACAIMBO'], 'VITORIA DE SANTO ANTAO': ['CHA DE ALEGRIA', 'CHA GRANDE', 'GLORIA DO GOITA', 'POMBOS', 'VITORIA DE SANTO ANTAO'] }
    
 
    cidade_encontrada = False
    for chave in regiao_cidades:
        if cidade in regiao_cidades[chave]:
            regiao = str(chave)
            cidade_encontrada=True
            break

    if cidade_encontrada==False:
        resultado.set('')
        aviso.set('Cidade não encontrada. ENTRE EM CONTATO COM A LOGÍSTICA')
        
    while cidade_encontrada:

        if regiao=='ALTO CAPIBARIBE':
            if cubagem<=15.99:
                valor_frete = cubagem*59
            elif 16<=cubagem<=40.99:
                valor_frete = cubagem*55
            elif 41<=cubagem<=59.99:
                valor_frete = cubagem*52
            else:
                valor_frete = cubagem*49
                
        if regiao=='ARARIPINA':
            if cubagem<=15.99:
                valor_frete = cubagem*80
            elif 16<=cubagem<=40.99:
                valor_frete = cubagem*77
            elif 41<=cubagem<=59.99:
                valor_frete = cubagem*74
            else:
                valor_frete = cubagem*70
                
        if regiao=='BREJO PERNAMBUCANO':
            if cubagem<=15.99:
                valor_frete = cubagem*52
            elif 16<=cubagem<=40.99:
                valor_frete = cubagem*49
            elif 41<=cubagem<=59.99:
                valor_frete = cubagem*45
            else:
                valor_frete = cubagem*42
                

        if regiao=='GARANHUNS' or regiao=='ITAPARICA' or regiao=='MATA MERIDIONAL PERNAMBUCANA' or regiao=='MATA SETENTRIONAL PERNAMBUCANA' or regiao=='MEDIO CAPIBARIBE':
            if cubagem<=15.99:
                valor_frete = cubagem*57
            elif 16<=cubagem<=40.99:
                valor_frete = cubagem*54
            elif 41<=cubagem<=59.99:
                valor_frete = cubagem*50
            else:
                valor_frete = cubagem*47
                    

        if regiao=='ITAMARACA' or regiao=='SUAPE':
            if cubagem<=15.99:
                valor_frete = cubagem*47
            elif 16<=cubagem<=40.99:
                valor_frete = cubagem*44
            elif 41<=cubagem<=59.99:
                valor_frete = cubagem*40
            else:
                valor_frete = cubagem*37
                        
        if regiao=='PAJEU':
            if cubagem<=15.99:
                valor_frete = cubagem*59
            elif 16<=cubagem<=40.99:
                valor_frete = cubagem*55
            elif 41<=cubagem<=59.99:
                valor_frete = cubagem*52
            else:
                valor_frete = cubagem*49         
        
        if regiao=='PETROLINA':
            if cubagem<=15.99:
                valor_frete = cubagem*70
            elif 16<=cubagem<=40.99:
                valor_frete = cubagem*67
            elif 41<=cubagem<=59.99:
                valor_frete = cubagem*64
            else:
                valor_frete = cubagem*60
                
        if regiao=='RECIFE' or regiao=='VITORIA DE SANTO ANTAO':
            if cubagem<=15.99:
                valor_frete = cubagem*49
            elif 16<=cubagem<=40.99:
                valor_frete = cubagem*45
            elif 41<=cubagem<=59.99:
                valor_frete = cubagem*42
            else:
                valor_frete = cubagem*39
                
        if regiao=='SALGUEIRO' or regiao=='SERTAO DO MOXOTO':
            if cubagem<=15.99:
                valor_frete = cubagem*60
            elif 16<=cubagem<=40.99:
                valor_frete = cubagem*57
            elif 41<=cubagem<=59.99:
                valor_frete = cubagem*54
            else:
                valor_frete = cubagem*50
                
        if regiao=='VALE DO IPANEMA' or regiao=='VALE DO IPOJUCA':
            if cubagem<=15.99:
                valor_frete = cubagem*52
            elif 16<=cubagem<=40.99:
                valor_frete = cubagem*49
            elif 41<=cubagem<=59.99:
                valor_frete = cubagem*45
            else:
                valor_frete = cubagem*42
            
        aviso.set('')
        resultado.set(f"Valor do frete: {valor_frete:.2f}")
        break

    

btn_calcular = Button(janela, text="Calcular", command=calcular)
btn_calcular.pack()

janela.mainloop()