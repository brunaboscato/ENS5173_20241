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

# Média de vazão mensal
media_vazao = vazao_media_mensal.mean()

# Meses com vazão abaixo da média (estiagem)
meses_estiagem = vazao_media_mensal[vazao_media_mensal < media_vazao].index.tolist()

# Meses com vazão acima da média (excesso)
meses_excesso = vazao_media_mensal[vazao_media_mensal > media_vazao].index.tolist()

# Plotar o hidrograma para a vazão média mensal
plt.figure(figsize=(10, 6))
plt.plot(vazao_media_mensal.index, vazao_media_mensal.values, marker='o', linestyle='-', color='b')

# Adicionando uma linha horizontal para a média da vazão
plt.axhline(y=media_vazao, color='r', linestyle='--', label=f'Média vazão: {media_vazao:.2f}')

# Destacando os meses de estiagem (abaixo da média)
plt.scatter(meses_estiagem, vazao_media_mensal[meses_estiagem], color='orange', label='Meses de Estiagem', zorder=5)

# Destacando os meses de excesso (acima da média)
plt.scatter(meses_excesso, vazao_media_mensal[meses_excesso], color='green', label='Meses de Excesso', zorder=5)

# Configuração do gráfico
plt.xlabel('Mês')
plt.ylabel('Vazão média mensal (m³/s)')
plt.xticks(ticks=np.arange(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
plt.tight_layout()
plt.legend()

# Exibindo o gráfico
plt.show()

# Exibindo os meses de estiagem e excesso no terminal
print(f"Meses de estiagem: {meses_estiagem}")
print(f"Meses de excesso: {meses_excesso}")
