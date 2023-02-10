# Interpolação de Lagrange

Este código usa o método de Interpolação de Lagrange para gerar um polinômio que aproxime uma função dada pelos pontos `x` e `y`.

## Bibliotecas

O código importa duas bibliotecas principais: `sympy` e `numpy`. A biblioteca `sympy` é usada para trabalhar com expressões matemáticas simbólicas e `numpy` é usada para trabalhar com arrays numéricos.

## Função `Lagrange`

A função `Lagrange` é responsável por calcular a interpolação de Lagrange. Ela recebe dois argumentos, `x` e `y`, que representam os pontos da função.

### Função aninhada `P`

A função `P` é uma função aninhada na função `Lagrange`. Ela recebe um argumento `z` e retorna o valor da função interpoladora em `z`.

#### Calculo das funções de Lagrange

A função `P` cria três matrizes `L1`, `L2` e `L3` para armazenar as funções de Lagrange correspondentes a cada ponto. Em seguida, ela calcula o valor da função interpoladora como a soma dos produtos de cada função de Lagrange pelo correspondente valor de `y`.

### Calculo do polinômio interpolador

A função `Lagrange` calcula as funções de Lagrange `L1`, `L2` e `L3` e em seguida, calcula o polinômio interpolador como a soma dos produtos de cada função de Lagrange pelo correspondente valor de `y`.

## Entrada de dados

O usuário é solicitado a informar os arrays `x` e `y` que representam os pontos de uma função. Eles são lidos como strings e convertidos para arrays de inteiros. Sua leitura deve ser feita todos em uma linha com espaçamentos

* Exemplo: `x: 1 2 3 4` e `y: 5 6 7 8`

## Chama a função Lagrange

O código chama a função `Lagrange` para obter o polinômio interpolador.

## Imprime o polinômio interpolador

O polinômio interpolador é simplificado e impresso na tela.

## Estimativa de x

O código apresenta o valor da estimativa para `x` especficado pelo usuário, substituindo o valor da incógnita `x` no polinômio interpolador. O resultado é apresentado como uma expressão simbólica e como um número arredondado.
