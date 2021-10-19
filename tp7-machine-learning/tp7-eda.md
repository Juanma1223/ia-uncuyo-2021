# Ejercicio 2

## a) La distribución de cantidad de árboles peligrosos se muestra en el siguiente gráfico, siendo 0 árboles no peligrosos y 1 árboles peligrosos, los primeros resultan ser la mayoría:

![img](https://github.com/Juanma1223/ia-uncuyo-2021/blob/main/tp7-machine-learning/plots/ej2-a.png)

## b) La sección que resultó ser mas peligrosa es la Residencial Sur

![img](https://github.com/Juanma1223/ia-uncuyo-2021/blob/main/tp7-machine-learning/plots/ej2-b.png)

## c) La especie mas peligrosa resultó la Morera

![img](https://github.com/Juanma1223/ia-uncuyo-2021/blob/main/tp7-machine-learning/plots/ej2-c.png)

# Ejercicio 3

## Histograma de frecuencia con la variable circunferencia en cm

![img](https://github.com/Juanma1223/ia-uncuyo-2021/blob/main/tp7-machine-learning/plots/ej3-a.png)

## Histograma de frecuencia con la variable circunferencia en cm pero habiendo filtrado solo árboles peligrosos

![img](https://github.com/Juanma1223/ia-uncuyo-2021/blob/main/tp7-machine-learning/plots/ej3-b.png)

# Ejercicio 4 (Desarrollo en el notebook de r con nombre part-a.rmd)

## Matriz de confusión

| n = 31912 | Inclinación peligrosa | Inclinación no peligrosa |
| --------- | --------------------- | ------------------------ |
| Acertó | 1779 | 14151 |
| Falló | 14182 | 1800 |

| n = 31912 | Inclinación peligrosa | Inclinación no peligrosa |
| --------- | --------------------- | ------------------------ |
| Positivo | 1779 | 1800 |
| Negativo | 14182 | 14151 |

# Ejercicio 5 (Desarrollo en el notebook de r con nombre part-a.rmd)

## Asignarle inclinación no peligrosa a todos por ser la clase mayoritaria

| n = 31912 | Inclinación peligrosa | Inclinación no peligrosa |
| --------- | --------------------- | ------------------------ |
| Positivo | 0 | 3579 |
| Negativo | 0 | 28333 |

# Ejercicio 6 

## Specificity y sensitivity del ejercicio 4:

Sensitivity = 1779/(1779+14182) = 0.11145918175

Specificity = 14151/(1800+14151) = 0.88715441038

## Specificity y sensitivity del ejercicio 5:

Sensitivity = 0

Specificity = 1
