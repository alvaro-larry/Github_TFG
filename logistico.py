import numpy as np
import matplotlib.pyplot as plt

# Parámetros
r = 0.1       # tasa intrínseca (>0)
K = 1000.0    # capacidad de carga (>0)
t_max = 100
t = np.linspace(0, t_max, 400)

# Valores iniciales: dos N0<K, el caso N0=K, dos N0>K
N0_list = [100.0, 500.0, 1500.0, 2000.0]

def logistic_N(t, r, K, N0):
    # Solución analítica: N(t) = K / (1 + A e^{-r t}), A = (K-N0)/N0
    A = (K - N0) / N0
    return K / (1 + A * np.exp(-r * t))

# Gráfica t vs N(t)
plt.figure()
for N0 in N0_list:
    N = logistic_N(t, r, K, N0)
    plt.plot(t, N, label=fr"$N_0 = {N0:g}$")
# línea horizontal en K para referencia
plt.axhline(K, color="k", linestyle="--", linewidth=0.7, label="K=1000")
plt.xlabel("Tiempo (años)")
plt.ylabel("Población")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(r"g:\Mi unidad\UCM\5º 2\TFG Física\logistico_multi_N.png", dpi=600, bbox_inches="tight")
plt.show()
