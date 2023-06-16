import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, x_values, y_values):
    """
    Função que realiza a interpolação de Lagrange.
    
    Argumentos:
    x -- O ponto em que queremos estimar a concentração de poluentes atmosféricos.
    x_values -- Lista das coordenadas x dos pontos de medição.
    y_values -- Lista das coordenadas y (concentração de poluentes) dos pontos de medição.
    
    Retorna:
    O valor interpolado da concentração de poluentes no ponto x.
    """
    n = len(x_values)
    interpolated_value = 0.0
    
    for i in range(n):
        # Calcula o polinômio de Lagrange Li(x) para o ponto i
        polynomial = 1.0
        for j in range(n):
            if i != j:
                polynomial *= (x - x_values[j]) / (x_values[i] - x_values[j])
        
        # Multiplica o polinômio de Lagrange pelo valor de y correspondente ao ponto i
        interpolated_value += y_values[i] * polynomial
    
    return interpolated_value


# Pontos de medição conhecidos
x_values = [2, 5, 7]
y_values = [4, 9, 11]

# Ponto para interpolação
x_interpolation = 4

# Calcula o valor interpolado
interpolated_value = lagrange_interpolation(x_interpolation, x_values, y_values)

print(f"O valor interpolado da concentração de poluentes em x = {x_interpolation} é: {interpolated_value}")

# Cria uma lista de valores x para plotagem suave da função original e do polinômio interpolador
x_plot = np.linspace(min(x_values), max(x_values), 100)
y_plot = lagrange_interpolation(x_plot, x_values, y_values)

# Plotagem da função original, dos pontos de medição e do polinômio interpolador
plt.plot(x_plot, y_plot, label='Polinômio Interpolador')
plt.plot(x_values, y_values, 'ro', label='Pontos da Função')
plt.plot(x_interpolation, interpolated_value, 'go', label='Ponto Interpolado')
plt.xlabel('x')
plt.ylabel('Concentração de Poluentes')
plt.title('Interpolação de Lagrange')
plt.legend()
plt.grid(True)
plt.show()