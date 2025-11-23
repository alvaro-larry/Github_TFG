import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
P0 = 100
t_max = 50
t = np.linspace(0, t_max, 200)

# Lista de tasas
r_values = [-0.05, -0.02, 0.0, 0.02, 0.05]

# Gráfica
plt.figure()
for r in r_values:
    P = P0 * np.exp(r * t)
    plt.plot(t, P, label=f"r = {r:.2%}")


plt.xlabel("Tiempo (años)")
plt.ylabel("Población")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(r"g:\Mi unidad\UCM\5º 2\TFG Física\malthus_multi_r.png", dpi=600, bbox_inches="tight")
plt.show()


plt.figure()
for r in r_values:
    lnP = np.log(P0) + r * t
    plt.plot(t, lnP, label=f"r = {r:.2%}")  # tiempo en X, ln(P) en Y

plt.xlabel("Tiempo (años)")
plt.ylabel("ln(Población)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(r"g:\Mi unidad\UCM\5º 2\TFG Física\malthus_lnN.png", dpi=600, bbox_inches="tight")
plt.show()
