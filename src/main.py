
from modules.dic_regiao_cidade import regiao_cidades
from modules.functions import *

cidade = input('Qual a cidade do destino?').upper()
cubagem = float(input('Qual o volume? (m\u00b3)').replace(',', '.'))
regiao =''

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
        valor_frete, valor_constante = function_1(cubagem)
        
                 
    if regiao=='ARARIPINA':
        valor_frete, valor_constante = function_2(cubagem)
        
      
    if regiao=='BREJO PERNAMBUCANO':
        valor_frete, valor_constante = function_3(cubagem)
        

    
    if regiao=='GARANHUNS' or regiao=='ITAPARICA' or regiao=='MATA MERIDIONAL PERNAMBUCANA' or regiao=='MATA SETENTRIONAL PERNAMBUCANA' or regiao=='MEDIO CAPIBARIBE':
        valor_frete, valor_constante = function_4(cubagem)
        

    if regiao=='ITAMARACA' or regiao=='SUAPE':
        valor_frete, valor_constante = function_5(cubagem)
        

    if regiao=='PAJEU':
        valor_frete, valor_constante = function_6(cubagem)  
        

    if regiao=='PETROLINA':
        valor_frete, valor_constante = function_7(cubagem)
        

    if regiao=='RECIFE' or regiao=='VITORIA DE SANTO ANTAO':
        valor_frete, valor_constante = function_8(cubagem)
        
    if regiao=='SALGUEIRO' or regiao=='SERTAO DO MOXOTO':
        valor_frete, valor_constante = function_9(cubagem)
        

    if regiao=='VALE DO IPANEMA' or regiao=='VALE DO IPOJUCA':
        valor_frete, valor_constante = function_10(cubagem)
        

    print(f'Valor do frete: R$ {valor_frete:.2f}')
    print(f'Valor tabelado do m\u00b3: {valor_constante}')    
   
    break

  
