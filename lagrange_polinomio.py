import numpy as np
import sympy as sp

"""
    Este trecho de código define a função "Lagrange", que tem como objetivo encontrar o polinômio interpolador de Lagrange. A função "Lagrange" recebe como entrada duas listas: uma com os 
    valores de x (os pontos onde se deseja interpolar a função) e outra com os valores de y (os valores da função nos pontos de x). A função "Lagrange" define uma outra função interna chamada 
    "P", que recebe como entrada um ponto "z" e retorna o valor da função interpoladora em "z". A função "P" usa as fórmulas de Lagrange para calcular o valor da função interpoladora em "z". 
    Cada fórmula de Lagrange pondera de uma forma diferente os valores de y para calcular o valor da função interpoladora em "z". A função "Lagrange" retorna o polinômio interpolador, que é 
    calculado como a soma dos produtos de cada fórmula de Lagrange pelo correspondente valor de y.
"""

def Lagrange(x, y):
    
    # Recebe três pontos (x, y) e retorna o polinômio interpolador de Lagrange.
    def P(z):
        
        # Recebe um ponto z e retorna o valor da função interpoladora em z.
        # Cria as matrizes L1, L2 e L3 para armazenar as funções de Lagrange correspondentes a cada ponto
        L1 = (z - x[1]) * (z - x[2]) / ((x[0] - x[1]) * (x[0] - x[2]))
        L2 = (z - x[0]) * (z - x[2]) / ((x[1] - x[0]) * (x[1] - x[2]))
        L3 = (z - x[0]) * (z - x[1]) / ((x[2] - x[0]) * (x[2] - x[1]))

        # Calcula o valor da função interpoladora como a soma dos produtos de cada função de Lagrange pelo correspondente valor de y
        return L1 * y[0] + L2 * y[1] + L3 * y[2]
    
    # Calcula as funções de Lagrande L1, L2 e L3. Cada uma corresponde em uma forma diferente de ponderar os valores
    x_sym = sp.symbols("x")
    L1 = (x_sym - x[1]) * (x_sym - x[2]) / ((x[0] - x[1]) * (x[0] - x[2]))
    L2 = (x_sym - x[0]) * (x_sym - x[2]) / ((x[1] - x[0]) * (x[1] - x[2]))
    L3 = (x_sym - x[0]) * (x_sym - x[1]) / ((x[2] - x[0]) * (x[2] - x[1]))
    
    # Calcula o polinômio interpolador como a soma dos produtos de cada função de Lagrange pelo correspondente valor de y
    return L1 * y[0] + L2 * y[1] + L3 * y[2]

# Pega os pontos x e y em uma array
x_str = input('Determine o array "x", adicionando os números separados por espaço: ').strip().split()
y_str = input('Determine o array "y", adicionando os números separados por espaço: ').strip().split()

# Expressão que está sendo buscada
est = input('Determine a estimativa desejada: ')

# Transforma os pontos de string para uma array de inteiros
x = np.array(x_str, dtype=int)
y = np.array(y_str, dtype=int)

# Chama a função Lagrange para obter o polinômio interpolador
P = Lagrange(x, y)

# Imprime o polinômio interpolador
print(f"\nO polinômio interpolador de Lagrange é: {sp.simplify(P)}\n")

# Apresenta o valor substituindo a incógnita 'x' pela número que buscamos, no caso é (x_0 + 2) 

x = sp.Symbol('x')
print(f"O resultado da estimado para o valor de f({est}) = {P.subs(x, 1)} -> {P.subs(x, 1).evalf()}")

