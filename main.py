cidade = input('Qual a cidade do destino?').upper()
cubagem = float(input('Qual o volume? (metros cúbicos)').replace(',', '.'))
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
    print('Cidade não encontrada. ENTRE EM CONTATO COM A LOGÍSTICA')
        

while cidade_encontrada:

    if regiao=='ALTO CAPIBARIBE':
        if cubagem <=7:
            valor_constante = 59
            valor_frete = 7*valor_constante
        elif 7<cubagem<=15.99:
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
        if cubagem <=7:
            valor_constante = 80
            valor_frete = 7*valor_constante
        elif 7<cubagem<=15.99:
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
        if cubagem <=7:
            valor_constante = 52
            valor_frete = 7*valor_constante
        elif 7<cubagem<=15.99:
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
        if cubagem <=7:
            valor_constante = 57
            valor_frete = 7*valor_constante
        elif 7<cubagem<=15.99:
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
        if cubagem <=7:
            valor_constante = 47
            valor_frete = 7*valor_constante
        elif 7<cubagem<=15.99:
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
        if cubagem <=7:
            valor_constante = 59
            valor_frete = 7*valor_constante
        elif 7<cubagem<=15.99:
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
        if cubagem <=7:
            valor_constante = 70
            valor_frete = 7*valor_constante
        elif 7<cubagem<=15.99:
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
        if cubagem <=7:
            valor_constante = 49
            valor_frete = 7*valor_constante
        elif 7<cubagem<=15.99:
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
        if cubagem <=7:
            valor_constante = 60
            valor_frete = 7*valor_constante
        elif 7<cubagem<=15.99:
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
        if cubagem <=7:
            valor_constante = 52
            valor_frete = 7*valor_constante
        elif 7<cubagem<=15.99:
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

    print(f'Valor do frete: {valor_frete:.2f}')
    print(f'Valor tabelado do m3: {valor_constante}')    
    break
    
