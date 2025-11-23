import numpy as np
import matplotlib.pyplot as plt

# Parámetros
r = 0.1       # tasa intrínseca
K = 1000.0    # capacidad de carga
A = 500.0     # umbral
t_max = 100
dt = 0.5
t = np.arange(0, t_max + dt, dt)

# Condiciones iniciales
N0_list = [100.0, 400.0, 600.0, 900.0, 1100.0, 1500.0]

# Función de crecimiento de Alle
def dN_dt(N, r, K, A):
    return r * N * (1 - N/K) * (N/A - 1)

# Método Runge-Kutta 4
def runge_kutta4(f, N0, t, r, K, A):
    N = np.zeros(len(t))
    N[0] = N0
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        k1 = f(N[i-1], r, K, A)
        k2 = f(N[i-1] + 0.5*k1*dt, r, K, A)
        k3 = f(N[i-1] + 0.5*k2*dt, r, K, A)
        k4 = f(N[i-1] + k3*dt, r, K, A)
        N[i] = N[i-1] + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
    return N

# Graficar soluciones
plt.figure(figsize=(8,6))
for N0 in N0_list:
    N = runge_kutta4(dN_dt, N0, t, r, K, A)
    plt.plot(t, N, label=fr"$N_0 = {N0:g}$")


# Dibujar asíntotas
plt.axhline(A, color='red', linestyle='--', linewidth=0.8, label=fr"A={A}")
plt.axhline(K, color='blue', linestyle='--', linewidth=0.8, label=fr"K={K}")

plt.xlabel("Tiempo (años)")
plt.ylabel("Población")
plt.grid(True)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig(r"g:\Mi unidad\UCM\5º 2\TFG Física\allee.jpg", dpi=600, bbox_inches="tight")
plt.show()
