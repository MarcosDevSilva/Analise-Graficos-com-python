import pandas
import plotly.express as px

dados = pandas.read_excel("vendas.xlsx")

# estatisticas
# dados.describe()

# analises
dados["loja"].value_counts()

# agrupando dados
#print(dados.groupby("loja")["preco"].sum())

# agrupando dados, em mais de uma coluna
dados_agrupado = dados.groupby(["loja", "cidade", "estado", "forma_pagamento"])["preco"].sum()

# criando arquivo excel
dados_agrupado.to_excel("Fatoramento.xlsx")




lista_colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]

for coluna in lista_colunas:
    graficos = px.histogram(dados, x=coluna,
                            y="preco",
                            text_auto=True,
                            title="Faturamento",
                            color="forma_pagamento")
    graficos.show()
    graficos.write_html(f"Faturamento-{coluna}.html")