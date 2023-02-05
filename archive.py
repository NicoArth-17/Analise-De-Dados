# Passo 1: Importar a base de dados

# Passo 2: Visualizar a base de dados
#   - Entender as informações disponíveis
#   - Descobrir os erros
 
# Passo 3: Tratamento de dados (resolver os erros)

# Passo 4: Analise inicial

# Passo 5: Analise detalhada (descobrir as causas dos cancelamentos)


# PASSO 1 - Importar usando o pandas

import pandas as pd

tabela = pd.read_csv("telecom_users.csv")



# PASSO 2 - Excluir informação desnecessária

tabela = tabela.drop('Unnamed: 0', axis=1) 
# axis = 0 -> linha  |  axis = 1 -> coluna



# PASSO 3 - Tratamento de dados (resolver os erros)
# 3.1 - Tratando variáveis erradas no valores

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
# ['nome da coluna'] -> selecionando a coluna
# .to_numeric() -> convertendo um valor em str que deveria ser numérico
# erros= -> tratando os erros
#           erros=ignore (ignorar)
#           erros=raise (mostrar o erro)
#           erros=coerce (forçar) , consequentimente o erro se tornará um valor vazio

# 3.2 - Tratando os valores vazios -- NaN (not a number)

tabela = tabela.dropna(how='all', axis=1) # Excluindo colunas vazias
# .dropna -> exclui valores vazios
# how='all' -> todos  | how='any' -> pelo menos um
# obs: coluna com todos os valores vazios não vao interferir nos dados, são descartaveis

tabela = tabela.dropna(how='any', axis=0) # Excluindo linhas vazias
# obs: linhas com todos algum valor vazio não pode interferir nos dados



# PASSO 4 - Analise inicial
# 4.1 - Contar os cancelamentos(churn) dos clientes

print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))
# normalize=True -> mostra os valores em porcentagem



# PASSO 5 - Analise detalhada (descobrir as causas dos cancelamentos)
# 5.1 - Comparar cada coluna da base de dados com a coluna 'Churn'

import plotly.express as px

# Gráfico para uma coluna |Início|
    # coluna = tabela['TipoContrato']   
    # grafico = px.histogram(tabela, x=coluna, color=tabela['Churn'], text_auto=True) # Cria o gráfico
        # coment.: .histogram -> tipo de grafico q mostra quantidades na base de dados
        # coment.: text_auto=True -> numerar as colonas do grafico

    # grafico.show() # Exibir o gráfico
# Gráfico para uma coluna |Fim|

#Gráfico para todas as colunas
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color=tabela['Churn'], text_auto=True)
    grafico.show()

print(tabela)
print(tabela.info()) # Mostra um resumo da tabela