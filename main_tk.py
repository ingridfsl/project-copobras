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


aviso = StringVar()
lbl_aviso = Label(janela, textvariable=aviso)
lbl_aviso.pack()

resultado = StringVar()

lbl_resultado = Label(janela, textvariable=resultado)
lbl_resultado.pack()

valor_fixo = StringVar()
lbl_aviso = Label(janela, textvariable=valor_fixo)
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
        valor_fixo.set('')
        aviso.set('Cidade não encontrada. ENTRE EM CONTATO COM A LOGÍSTICA')
        
    while cidade_encontrada:

        if regiao=='ALTO CAPIBARIBE':
            if cubagem<=15.99:
                valor_constante = 59
                valor_frete = cubagem * valor_constante    
            elif 16<=cubagem<=40.99:
                valor_constante = 55
                valor_frete = cubagem*valor_constante 
            elif 41<=cubagem<=59.99:
                valor_constante=52
                valor_frete = cubagem*valor_constante 
            else:
                valor_constante = 49
                valor_frete = cubagem*valor_constante 
                
        if regiao=='ARARIPINA':
            if cubagem<=15.99:
                valor_constante = 80
                valor_frete = cubagem*valor_constante
            elif 16<=cubagem<=40.99:
                valor_constante = 77
                valor_frete = cubagem*valor_constante
            elif 41<=cubagem<=59.99:
                valor_constante = 74
                valor_frete = cubagem*valor_constante
            else:
                valor_constante = 70
                valor_frete = cubagem*valor_constante
                
        if regiao=='BREJO PERNAMBUCANO':
            if cubagem<=15.99:
                valor_constante = 52
                valor_frete = cubagem*valor_constante
            elif 16<=cubagem<=40.99:
                valor_constante = 49
                valor_frete = cubagem*valor_constante
            elif 41<=cubagem<=59.99:
                valor_constante = 45
                valor_frete = cubagem*valor_constante
            else:
                valor_constante = 42
                valor_frete = cubagem*valor_constante
                

        if regiao=='GARANHUNS' or regiao=='ITAPARICA' or regiao=='MATA MERIDIONAL PERNAMBUCANA' or regiao=='MATA SETENTRIONAL PERNAMBUCANA' or regiao=='MEDIO CAPIBARIBE':
            if cubagem<=15.99:
                valor_constante = 57
                valor_frete = cubagem*valor_constante
            elif 16<=cubagem<=40.99:
                valor_constante = 54
                valor_frete = cubagem*valor_constante
            elif 41<=cubagem<=59.99:
                valor_constante = 50
                valor_frete = cubagem*valor_constante
            else:
                valor_constante = 47
                valor_frete = cubagem*valor_constante
                    

        if regiao=='ITAMARACA' or regiao=='SUAPE':
            if cubagem<=15.99:
                valor_constante = 47
                valor_frete = cubagem*valor_constante
            elif 16<=cubagem<=40.99:
                valor_constante = 44
                valor_frete = cubagem*valor_constante
            elif 41<=cubagem<=59.99:
                valor_constante = 40
                valor_frete = cubagem*valor_constante
            else:
                valor_constante = 37
                valor_frete = cubagem*valor_constante
                        
        if regiao=='PAJEU':
            if cubagem<=15.99:
                valor_constante = 59
                valor_frete = cubagem*valor_constante
            elif 16<=cubagem<=40.99:
                valor_constante = 55
                valor_frete = cubagem*valor_constante
            elif 41<=cubagem<=59.99:
                valor_constante = 52
                valor_frete = cubagem*valor_constante
            else:
                valor_constante = 49
                valor_frete = cubagem*valor_constante         
        
        if regiao=='PETROLINA':
            if cubagem<=15.99:
                valor_constante = 70
                valor_frete = cubagem*valor_constante
            elif 16<=cubagem<=40.99:
                valor_constante = 67
                valor_frete = cubagem*valor_constante
            elif 41<=cubagem<=59.99:
                valor_constante = 64
                valor_frete = cubagem*valor_constante
            else:
                valor_constante = 60
                valor_frete = cubagem*valor_constante
                
        if regiao=='RECIFE' or regiao=='VITORIA DE SANTO ANTAO':
            if cubagem<=15.99:
                valor_constante = 49
                valor_frete = cubagem*valor_constante
            elif 16<=cubagem<=40.99:
                valor_constante = 45
                valor_frete = cubagem*valor_constante
            elif 41<=cubagem<=59.99:
                valor_constante = 42
                valor_frete = cubagem*valor_constante
            else:
                valor_constante = 39
                valor_frete = cubagem*valor_constante
                
        if regiao=='SALGUEIRO' or regiao=='SERTAO DO MOXOTO':
            if cubagem<=15.99:
                valor_constante = 60
                valor_frete = cubagem*valor_constante
            elif 16<=cubagem<=40.99:
                valor_constante = 57
                valor_frete = cubagem*valor_constante
            elif 41<=cubagem<=59.99:
                valor_constante = 54
                valor_frete = cubagem*valor_constante
            else:
                valor_constante = 50
                valor_frete = cubagem*valor_constante
                
        if regiao=='VALE DO IPANEMA' or regiao=='VALE DO IPOJUCA':
            if cubagem<=15.99:
                valor_constante = 52
                valor_frete = cubagem*valor_constante
            elif 16<=cubagem<=40.99:
                valor_constante = 49
                valor_frete = cubagem*valor_constante
            elif 41<=cubagem<=59.99:
                valor_constante = 45
                valor_frete = cubagem*valor_constante
            else:
                valor_constante = 42
                valor_frete = cubagem*valor_constante
            
        aviso.set('')
        valor_fixo.set(f'Valor tabelado do m3: {valor_constante}')
        resultado.set(f"Valor do frete: {valor_frete:.2f}")
        break

    

btn_calcular = Button(janela, text="Calcular", command=calcular)
btn_calcular.pack()

janela.mainloop()