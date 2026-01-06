import numpy as np
import matplotlib.pyplot as plt

# Parámetros
P0 = 100
t_max = 50
t = np.linspace(0, t_max, 200)

# Tasas de crecimiento en orden de curvas (de mayor a menor)
r_values = [0.05, 0.02, 0.0, -0.02, -0.05]

# Configuración general de tamaño de fuente
plt.rcParams.update({'font.size': 14})  

# Gráfico P(t)
plt.figure(figsize=(7,5))
for r in r_values:
    P = P0 * np.exp(r * t)
    plt.plot(t, P, label=f"r = {r:.2f}") 

plt.xlabel("Tiempo")
plt.ylabel("Población")
plt.grid(True)
plt.legend(edgecolor='black' )
plt.tight_layout()
plt.savefig("malthus_multi_r.png", dpi=600)
plt.show()

# Gráfico ln(P)
plt.figure(figsize=(7,5))
for r in r_values:
    lnP = np.log(P0) + r * t
    plt.plot(t, lnP, label=f"r = {r:.2f}")

plt.xlabel("Tiempo (años)")
plt.ylabel("ln(Población)")
plt.grid(True)
plt.legend(edgecolor='black' )
plt.tight_layout()
plt.savefig("malthus_lnN.png", dpi=600)
plt.show()