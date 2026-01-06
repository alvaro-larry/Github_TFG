import numpy as np
import matplotlib.pyplot as plt

# Parámetros
r = 0.1
K = 1000.0
t_max = 100
t = np.linspace(0, t_max, 400)

# Valores iniciales (ordenados como las curvas)
N0_values = [2000.0, 1500.0, 500.0, 100.0]

# Configuración general de tamaño de fuente
plt.rcParams.update({'font.size': 14})

def logistic_N(t, r, K, N0):
    A = (K - N0) / N0
    return K / (1 + A * np.exp(-r * t))

# Gráfica N(t)
plt.figure(figsize=(7,5))
for N0 in N0_values:
    N = logistic_N(t, r, K, N0)
    plt.plot(t, N, label=fr"$N_0 = {N0:g}$")

# Línea de referencia en K
plt.axhline(K, linestyle="--", linewidth=1.0, color='purple', label=r"$K=1000$")

plt.xlabel("Tiempo")
plt.ylabel("Población")
plt.grid(True)
plt.legend(edgecolor='black' )
plt.tight_layout()
plt.savefig("logistico_multi_N.png", dpi=800)
plt.show()
