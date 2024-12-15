import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dados de precipitação para o período de 1991-2020
precipitacao = {
    'Janeiro': 226.6,
    'Fevereiro': 236.1,
    'Março': 275.4,
    'Abril': 110.5,
    'Maio': 47.9,
    'Junho': 18.9,
    'Julho': 7.4,
    'Agosto': 10.3,
    'Setembro': 59.2,
    'Outubro': 136.6,
    'Novembro': 200.0,
    'Dezembro': 264.4
}

# Caminho da planilha
file_path = r"C:\Users\bruna\OneDrive\Área de Trabalho\TrabalhoHidro\Hist.xlsx"

# Lendo a planilha
df = pd.read_excel(file_path)

# Garantir que a coluna 'Data' esteja no formato de data
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Criar uma nova coluna para o mês
df['Mês'] = df['Data'].dt.month

# Calcular a vazão média mensal
vazao_media_mensal = df.groupby('Mês')['Vazao media'].mean()

# Definir os meses do ano
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
meses_num = np.arange(1, 13)

# Plotar o gráfico comparativo entre vazão média e precipitação
fig, ax1 = plt.subplots(figsize=(12, 6))

# Gráfico de vazão média mensal
ax1.set_xlabel('Meses')
ax1.set_ylabel('Vazão média mensal (m³/s)', color='tab:blue')
ax1.plot(meses_num, vazao_media_mensal.values, marker='o', color='tab:blue', label='Vazão média mensal')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Criar um eixo secundário para a precipitação
ax2 = ax1.twinx()  
ax2.set_ylabel('Precipitação (mm)', color='tab:green')  
ax2.plot(meses_num, list(precipitacao.values()), marker='s', color='tab:green', label='Precipitação (mm)')
ax2.tick_params(axis='y', labelcolor='tab:green')

# Adicionar título e ajustar labels dos meses
plt.title('Comparação entre Vazão Média Mensal e Precipitação (1991-2020)')
ax1.set_xticks(meses_num)
ax1.set_xticklabels(meses)
fig.tight_layout()

# Exibir o gráfico
plt.show()

# Análise da relação entre precipitação e vazão
correlacao = pd.Series(list(precipitacao.values()), index=meses_num) 
correlacao = correlacao - vazao_media_mensal.values

# Verificar quais meses têm maior ou menor correlação com precipitação e vazão
meses_positivos = correlacao[correlacao > 0].index.tolist()
meses_negativos = correlacao[correlacao < 0].index.tolist()

print(f"Meses com maior precipitação que vazão (excesso de chuva): {meses_positivos}")
print(f"Meses com menor precipitação que vazão (possível estiagem): {meses_negativos}")
