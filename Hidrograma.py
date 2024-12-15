import pandas as pd
import matplotlib.pyplot as plt

# Caminho da planilha
file_path = r"C:\Users\bruna\OneDrive\Área de Trabalho\TrabalhoHidro\Hist.xlsx"

# Lendo a planilha
df = pd.read_excel(file_path)

# Garantir que a coluna 'Data' esteja no formato de data
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Plotar o hidrograma (Vazão média x Tempo)
plt.figure(figsize=(10, 6))
plt.plot(df['Data'], df['Vazao media'], label='Vazão média', color='blue')
plt.xlabel('Data')
plt.ylabel('Vazão média (m³/s)')
plt.title('Hidrograma - Vazão média ao longo do tempo')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
