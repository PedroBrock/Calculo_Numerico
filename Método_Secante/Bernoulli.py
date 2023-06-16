import math
import numpy as np
import matplotlib.pyplot as plt

def bernoulli(f, x0, x1, tol):
    while abs(f(x1)) > tol:
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_next

    return x1

# Definindo os parâmetros do problema
q = 0.1   # vazão (m³/s)
D = 0.05  # diâmetro interno do tubo (m)
g = 9.81  # aceleração da gravidade (m/s²)
rho = 1000  # densidade da água (kg/m³)
L = 100  # comprimento do tubo (m)
epsilon = 0.00001  # rugosidade absoluta (m)
P1 = 1e5  # pressão no ponto 1 (Pa)
P2 = 0  # pressão no ponto 2 (Pa)

# Definindo a função a ser resolvida
def f(x):
    return (4 * q**2 * epsilon / (math.pi**2 * D**8 * 2 * g * rho) * L * x**2
            + P2 / rho - P1 / rho - x)

# Resolvendo a equação de Bernoulli
x0 = 1  # chute inicial
x1 = 2  # chute inicial
tol = 1e-6  # tolerância para o critério de parada
x = bernoulli(f, x0, x1, tol)

# Plotando a função e a raiz encontrada
x_vals = np.linspace(0, 5, 1000)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='Função')
plt.axhline(y=0, color='black', linestyle='--')
plt.scatter(x, f(x), color='red', label='Raiz')
plt.xlabel('Velocidade (m/s)')
plt.ylabel('Função')
plt.legend()
plt.show()

# Imprimindo o resultado
print('A velocidade no ponto 2 é de', x, 'm/s')