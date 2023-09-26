# Importando bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definición del sistema de ecuaciones de Lorenz
def lorenz_system(current, t, sigma, beta, rho):
    # 'current' contiene los valores actuales de x, y, z.
    # 't' es el tiempo actual.
    # 'sigma', 'beta', 'rho' son los parámetros del sistema de Lorenz.

    x, y, z = current  # Desempaquetar el estado actual en variables individuales

    # dx/dt = sigma * (y - x)
    # Esta ecuación representa la tasa de cambio de x con respecto al tiempo.
    # Está influenciada por la diferencia entre los valores actuales de y y x, escalada por sigma.
    dx_dt = sigma * (y - x)

    # dy/dt = x * (rho - z) - y
    # Esta ecuación representa la tasa de cambio de y con respecto al tiempo.
    # Involucra una combinación de los valores actuales de x, y y z, y el parámetro rho.
    dy_dt = x * (rho - z) - y

    # dz/dt = x * y - beta * z
    # Esta ecuación representa la tasa de cambio de z con respecto al tiempo.
    # Involucra los valores actuales de x y y, así como el parámetro beta.
    dz_dt = x * y - beta * z

    return [dx_dt, dy_dt, dz_dt]  # Devolver lista de tasas de cambio


# Parámetros y condiciones iniciales
sigma, beta, rho = 10, 2.667, 28
initial = [0, 2, 20]

# Puntos de tiempo
t = np.linspace(0, 50, 5000)

# Resolver las ecuaciones diferenciales
solution = odeint(lorenz_system, initial, t, args=(sigma, beta, rho))

# Extraer las matrices individuales de valores x, y y z de la solución
x, y, z = solution.T

# Graficar
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z, lw=0.5)
ax.set_title("Lorenz Attractor")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.show()
