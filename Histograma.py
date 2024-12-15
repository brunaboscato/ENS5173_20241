import pandas as pd
import matplotlib.pyplot as plt

# Caminho da planilha
file_path = r"C:\Users\bruna\OneDrive\Área de Trabalho\TrabalhoHidro\Hist.xlsx"

# Lendo a planilha
df = pd.read_excel(file_path)

# Convertendo a coluna de datas para datetime no formato DD/MM/YYYY
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Histograma das vazões diárias
plt.figure(figsize=(10, 6))
plt.hist(df['Vazao media'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Vazão média (m³/s)')
plt.ylabel('Frequência')
plt.title('Histograma das Vazões Diárias')
plt.grid(True)
plt.tight_layout()
plt.show()
