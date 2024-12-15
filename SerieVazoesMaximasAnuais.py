import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Caminho da planilha
file_path = r"C:\Users\bruna\OneDrive\Área de Trabalho\TrabalhoHidro\Hist.xlsx"

# Lendo a planilha
df = pd.read_excel(file_path)

# Garantir que a coluna 'Data' esteja no formato de data
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Criar uma nova coluna para o ano
df['Ano'] = df['Data'].dt.year

# Calcular a série de vazões máximas anuais
vazao_maxima_anual = df.groupby('Ano')['Vazao media'].max()

# Plotando a série de vazões máximas anuais (Gráfico de linha)
plt.figure(figsize=(10, 6))
plt.plot(vazao_maxima_anual.index, vazao_maxima_anual.values, marker='o', color='b', label='Vazão Máxima Anual')
plt.xlabel('Ano')
plt.ylabel('Vazão Máxima (m³/s)')
plt.title('Série de Vazões Máximas Anuais')
plt.grid(True)

# Adicionando linha de tendência (regressão linear)
slope, intercept, r_value, p_value, std_err = linregress(vazao_maxima_anual.index, vazao_maxima_anual.values)
plt.plot(vazao_maxima_anual.index, slope * vazao_maxima_anual.index + intercept, 'r--', label='Linha de Tendência')

# Exibindo a legenda
plt.legend()
plt.tight_layout()
plt.show()
