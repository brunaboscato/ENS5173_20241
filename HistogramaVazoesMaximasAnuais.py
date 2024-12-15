import pandas as pd
import matplotlib.pyplot as plt

# Caminho da planilha
file_path = r"C:\Users\bruna\OneDrive\Área de Trabalho\TrabalhoHidro\Hist.xlsx"

# Lendo a planilha
df = pd.read_excel(file_path)

# Garantir que a coluna 'Data' esteja no formato de data
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Extrair o ano da coluna 'Data'
df['Ano'] = df['Data'].dt.year

# Calcular as vazões máximas anuais
vazao_maxima_anual = df.groupby('Ano')['Vazao media'].max()

# Plotando o histograma das vazões máximas anuais
plt.figure(figsize=(10, 6))
plt.hist(vazao_maxima_anual, bins=10, color='lightblue', edgecolor='black')
plt.xlabel('Vazão Máxima Anual (m³/s)')
plt.ylabel('Frequência')
plt.title('Histograma das Vazões Máximas Anuais')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Exibindo estatísticas descritivas para a análise
print(vazao_maxima_anual.describe())
