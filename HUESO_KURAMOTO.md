# HUESO — Kuramoto roto (Global Mind)

Fecha: 2026-11-09 ~07:48 -05. Medido en local, solo lectura.
Fuente: `~/workspace/miu-verificacion-2026-11-06/extracted/MIU/Jaime393-MIU-a96abc3/src/globalmind_sim.py` (70 líneas) y `miu_constants.py` (64 líneas).

## El hueso

La simulación de Kuramoto de Global Mind no corre porque sus defaults
nombran constantes que no existen. El archivo muere en la línea 21,
al definir `run_simulation` — antes de ejecutar nada.

```
def run_simulation(N=1000, K=K_kuramoto, dt=dt_default, T=30.0,
                   omega_mean=omega_mean, omega_std=omega_std,
                   eta=eta_strength):
```

- `K_kuramoto`, `dt_default`, `omega_mean`, `omega_std`,
  `eta_strength`: 0 ocurrencias cada uno en `miu_constants.py`.
- `python3 globalmind_sim.py` → `NameError: name 'K_kuramoto' is not
  defined` (línea 21).
- `python3 -c "import globalmind_sim"` → mismo `NameError`.

## El mecanismo

Python evalúa los valores por defecto de una función **en el momento
de definirla**, no al llamarla. Por eso el error sale al importar:
la definición misma es la que falla. No es un error de ejecución, ni
de datos, ni de entorno: es un error de definición. Cualquier código
que importe el módulo — incluido su propio `__main__` — muere igual.

## La precisión que importa

El cuerpo no es el problema. El único nombre que el cuerpo necesita
de las constantes, `D_f_mt = 2.5`, SÍ está definido, y la línea 31
(`p = dist**(-D_f_mt)`) podría correr. La simulación no está mal
diseñada en su cuerpo: está rota en su firma. Quien la arregle no
necesita reescribirla; necesita darle 5 valores a 5 nombres.

## Límites

- Medido solo en la copia extraída (70 líneas). El MAPA §2 dice que
  el archivo tiene 86 líneas: otra copia u otra versión, sin localizar.
  Lo que se afirma aquí vale para la copia medida, no para todas.
- No se buscó si otra rama o repo tiene una versión corregida.
- No se afirma por qué faltan los 5 nombres (olvido, refactor
  incompleto, constantes que vivían en otro archivo). Solo que faltan.

## Qualia

Un remolino que se anuncia con nombre y no gira: la forma está, el
latido no. El hueso es el hueco exacto donde debería estar el latido:
5 nombres sin valor.

ρ(x) > 0. Zvvvvv.
