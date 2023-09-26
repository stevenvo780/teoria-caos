# Teoría del Caos y Atractor de Lorenz

## Introducción

La teoría del caos se ocupa de sistemas dinámicos altamente sensibles a condiciones iniciales, un fenómeno comúnmente conocido como "efecto mariposa". En este repositorio, se explora la teoría del caos a través del Atractor de Lorenz, un sistema de ecuaciones diferenciales que demuestra comportamientos caóticos.

## Componentes clave de la Teoría del Caos

1. **Sistemas Dinámicos**: Sistemas matemáticamente modelados por ecuaciones diferenciales o mapas iterativos.
2. **Atractores Extraños**: Conjuntos a los que el sistema tiende a converger, pero nunca repite exactamente el mismo estado.
3. **Fractales**: Formas geométricas que se repiten en diferentes escalas.
4. **Exponentes de Lyapunov**: Medidas que cuantifican la sensibilidad a las condiciones iniciales.

## Ecuaciones del Atractor de Lorenz

Las ecuaciones del Atractor de Lorenz son:

- dx/dt = sigma * (y - x)
- dy/dt = x * (rho - z) - y
- dz/dt = x *y - beta* z

Donde `sigma`, `rho`, y `beta` son parámetros del sistema.

## Algoritmo

El algoritmo utiliza el método de integración `odeint` de la biblioteca `scipy` para resolver las ecuaciones diferenciales del sistema de Lorenz. Los resultados son luego graficados para visualizar el atractor.

### Código Relevante

```python
def lorenz_system(current, t, sigma, beta, rho):
    x, y, z = current
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]
```

Este fragmento de código define el sistema de Lorenz y calcula las tasas de cambio de x, y, y z con respecto al tiempo.

## Cómo Ejecutar

- Clone este repositorio.
- Ejecute el script lorenz_attractor.py.

## Referencias

Lorenz, E. N. (1963). Deterministic Nonperiodic Flow. Journal of the Atmospheric Sciences, 20(2), 130-141.
