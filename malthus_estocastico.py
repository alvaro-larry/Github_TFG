import numpy as np
import matplotlib.pyplot as plt

# Parámetros
r = 0.5        # tasa de crecimiento
sigma = 0.2    # intensidad del ruido
N0 = 10        # valor inicial
T = 10         # tiempo total
dt = 0.001     # paso temporal
n = int(T/dt)  # número de pasos

# Arrays
t = np.linspace(0, T, n)
N = np.zeros(n)
N[0] = N0

# Simulación Euler-Maruyama
for i in range(1, n):
    dW = np.sqrt(dt) * np.random.randn()
    N[i] = N[i-1] + r*N[i-1]*dt + sigma*N[i-1]*dW

# Gráfica
plt.plot(t, N)
plt.xlabel("Tiempo")
plt.ylabel("N(t)")
plt.title("Proceso estocástico Malthus (Euler–Maruyama)")
plt.show()

for j in range(5):  # 5 trayectorias
    N = np.zeros(n)
    N[0] = N0
    for i in range(1, n):
        dW = np.sqrt(dt) * np.random.randn()
        N[i] = N[i-1] + r*N[i-1]*dt + sigma*N[i-1]*dW

    plt.plot(t, N)

plt.xlabel("Tiempo")
plt.ylabel("N(t)")
plt.title("Varias trayectorias del proceso de Malthus estocástico")
plt.show()
