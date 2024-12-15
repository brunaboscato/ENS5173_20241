import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Calcular o coeficiente de variação
desvio_padrao = df.groupby('Mês')['Vazao media'].std()
media_vazao = df.groupby('Mês')['Vazao media'].mean()
coeficiente_variacao = (desvio_padrao / media_vazao) * 100

# Exibir o coeficiente de variação
print("Coeficiente de variação por mês:")
print(coeficiente_variacao)

# Plotando a média de vazão por mês (Gráfico de barras)
plt.figure(figsize=(10, 6))
plt.bar(vazao_media_mensal.index, vazao_media_mensal.values, color='skyblue', edgecolor='black')
plt.xlabel('Mês')
plt.ylabel('Vazão média mensal (m³/s)')
plt.title('Vazão Média Mensal')
plt.xticks(ticks=np.arange(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Plotando o coeficiente de variação por mês (Gráfico de barras)
plt.figure(figsize=(10, 6))
plt.bar(coeficiente_variacao.index, coeficiente_variacao.values, color='salmon', edgecolor='black')
plt.xlabel('Mês')
plt.ylabel('Coeficiente de variação (%)')
plt.title('Coeficiente de Variação das Vazões por Mês')
plt.xticks(ticks=np.arange(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(axis='y')
plt.tight_layout()
plt.show()

