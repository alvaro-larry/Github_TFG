import numpy as np
import matplotlib.pyplot as plt

# Parámetros
r = 0.1       # tasa intrínseca
K = 1000.0    # capacidad de carga
A = 500.0     # umbral de Allee
t_max = 100
dt = 0.5
t = np.arange(0, t_max + dt, dt)

# Condiciones iniciales
N0_list = [1500.0, 1100.0, 900.0, 600.0, 400.0, 100.0]

# Configuración general de tamaño de fuente (CLAVE)
plt.rcParams.update({'font.size': 14})

# Función de crecimiento de Allee
def dN_dt(N, r, K, A):
    return r * N * (1 - N/K) * (N/A - 1)

# Método Runge–Kutta de cuarto orden
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

# Gráfica
plt.figure(figsize=(7,5))
for N0 in N0_list:
    N = runge_kutta4(dN_dt, N0, t, r, K, A)
    plt.plot(t, N, label=fr"$N_0 = {N0:g}$")

# Líneas de referencia
plt.axhline(K, linestyle="--", linewidth=1.0, color='blue', label=fr"$K={K:g}$")
plt.axhline(A, linestyle="--", linewidth=1.0, color='red', label=fr"$A={A:g}$")


plt.xlabel("Tiempo")
plt.ylabel("Población")
plt.grid(True)
plt.legend(
    loc='upper center',         # posición arriba
    bbox_to_anchor=(0.60, 1.15), # fuera del gráfico
    ncol=3,                     # número de columnas
    frameon=True,                # dibuja el cuadro
    fancybox=True,               # bordes redondeados
    framealpha=1.0,              # opacidad del fondo (0 transparente, 1 sólido)
    edgecolor='black'            # color del borde
)


plt.tight_layout()
plt.savefig("allee.png", dpi=800)
plt.show()
