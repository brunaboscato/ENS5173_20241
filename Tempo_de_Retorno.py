import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gumbel_r, lognorm

# Caminho da planilha
file_path = r"C:\Users\bruna\OneDrive\Área de Trabalho\TrabalhoHidro\Hist.xlsx"

# Lendo a planilha
df = pd.read_excel(file_path)

# Garantir que a coluna 'Data' esteja no formato de data (caso ainda não tenha feito isso)
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Função para calcular o tempo de retorno empírico
def calcular_tempos_retorno(vazao_maxima):
    n = len(vazao_maxima)
    vazao_maxima_sorted = np.sort(vazao_maxima)[::-1]  # Ordenar em ordem decrescente
    tempos_retorno = (n + 1) / (np.arange(1, n+1))  # Tempo de retorno empírico
    return vazao_maxima_sorted, tempos_retorno

# Função para estimar a distribuição Lognormal
def lognormal_fit(vazao_maxima):
    shape, loc, scale = lognorm.fit(vazao_maxima, floc=0)
    return shape, loc, scale

# Função para estimar a distribuição Gumbel
def gumbel_fit(vazao_maxima):
    loc, scale = gumbel_r.fit(vazao_maxima)
    return loc, scale

# Função para calcular a estimativa da vazão para um dado tempo de retorno
def estimar_vazao_lognormal(tempos_retorno, shape, loc, scale):
    return lognorm.ppf(1 - 1/tempos_retorno, shape, loc, scale)

def estimar_vazao_gumbel(tempos_retorno, loc, scale):
    return gumbel_r.ppf(1 - 1/tempos_retorno, loc, scale)

# Calcular o tempo de retorno empírico
vazao_maxima_sorted, tempos_retorno = calcular_tempos_retorno(df['Vazao maxima'])

# Estimar os parâmetros das distribuições
shape_lognormal, loc_lognormal, scale_lognormal = lognormal_fit(df['Vazao maxima'])
loc_gumbel, scale_gumbel = gumbel_fit(df['Vazao maxima'])

# Estimar as vazões associadas aos tempos de retorno para ambas as distribuições
vazao_lognormal = estimar_vazao_lognormal(tempos_retorno, shape_lognormal, loc_lognormal, scale_lognormal)
vazao_gumbel = estimar_vazao_gumbel(tempos_retorno, loc_gumbel, scale_gumbel)

# Calcular o erro quadrático médio (EQM) para as distribuições
eqm_lognormal = np.mean((vazao_maxima_sorted - vazao_lognormal[:len(vazao_maxima_sorted)])**2)
eqm_gumbel = np.mean((vazao_maxima_sorted - vazao_gumbel[:len(vazao_maxima_sorted)])**2)

print(f"Erro Quadrático Médio Lognormal: {eqm_lognormal}")
print(f"Erro Quadrático Médio Gumbel: {eqm_gumbel}")

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(tempos_retorno, vazao_maxima_sorted, 'o', label='Vazão Máxima Observada')
plt.plot(tempos_retorno, vazao_lognormal, label='Estimativa Lognormal', linestyle='--')
plt.plot(tempos_retorno, vazao_gumbel, label='Estimativa Gumbel', linestyle='--')
plt.xlabel('Tempo de Retorno (anos)')
plt.ylabel('Vazão Máxima (m³/s)')
plt.title('Estimativas das Vazões Máximas Anuais com Lognormal e Gumbel')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
