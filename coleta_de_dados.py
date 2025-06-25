import pandas as pd
import os

os.makedirs('dados_tratados', exist_ok=True)

#Carregar o csv
df = None
try:
    df = pd.read_csv('fonte-dados/customers-100.csv')
except Exception as erro:
    print('Erro ao carregar o csv: ',erro)

#Verificar se o arquivo foi carregado
if(df is not None):
    #salva o arquivo como excel
    if(not os.path.exists('dados_tratados/todos_dados.xlsx')):
        try:
            df.to_excel('dados_tratados/todos_dados.xlsx')
            print('Arquivo salvo com sucesso!')
        except Exception as erro:
            print('Falha ao salvar o arquivo em excel: ',erro)
    
    #limpando dados onde data de inscrição é maior que 2022
    sub_date = pd.to_datetime(df["Subscription Date"])
    anos_sub_date = sub_date.dt.year
    sub_date_2022 = df[anos_sub_date == 2022]
    if(not sub_date_2022.empty):
        #Filtrar Nome, Email e Data de inscrição e ordena por Nome
        dados_filtrados = sub_date_2022.loc[:,['First Name','Email','Subscription Date']].sort_values('First Name')
        try:
            dados_filtrados.to_excel('dados_tratados/inscricao_2022.xlsx')
            print('Arquivo salvo com sucesso!, Inscrições feitas em 2022')
        except Exception as erro:
            print('Falha ao salvar o arquivo, erro: ',erro)
    else:
        print('Não encontrou nenhum dado com data igual a 2022')
else:
    print('o arquivo csv não foi carregado.')