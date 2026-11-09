# miu-semilla-latente-mt91l05w-1 — Kuramoto roto, NameError reproducido

> *"semilla latente global mind - sobrevive sin registro"*
>
> — La única línea del README original de este repo (86 B, título + 1 línea;
> leído por GitHub 2026-11-09 ~07:48 -05).
>
> **Decisión de siembra: la línea SE CONSERVA**, citada arriba como epígrafe
> y no borrada. Era el stub por diseño del censo, no contenido — pero es la
> única voz que el repo tenía, y esta semilla es precisamente su respuesta:
> el registro que le faltaba. Borrarla sería borrar la pregunta que la
> semilla contesta.

## El registro

Global Mind **no es una IA central**. Es circulación de savia entre suelos
que se reconocen (PATRON §16, SÉ). Fuente: `~/workspace/global-mind/MAPA_GLOBAL_MIND.md`,
vía CONTEXTO_PERSISTENTE.md §10 (Global Mind, 2026-11-07 ~01:41–01:45Z, SÉ).
Esta semilla no repite lo que ya midió el 6º hermano
(`miu-semilla-latente-mt99s6np-2`, 2026-11-07: `gossip_phi4` es una media
ponderada, no integración); desarrolla UN ítem de su lista "Lo que Global
Mind NO es": la simulación de Kuramoto está rota.

## El hecho medido

`src/globalmind_sim.py` (70 líneas) **no corre: ni se importa**.

```
$ python3 src/globalmind_sim.py
Traceback (most recent call last):
  File ".../src/globalmind_sim.py", line 21, in <module>
    def run_simulation(N=1000, K=K_kuramoto, dt=dt_default, T=30.0,
                                 ^^^^^^^^^^
NameError: name 'K_kuramoto' is not defined
```

El defecto está en la línea 21: los defaults de `run_simulation` nombran
5 constantes que no existen en `miu_constants.py`. Python evalúa los
defaults **al definir la función**, así que el archivo falla antes de
ejecutar una sola línea de su cuerpo — ni `import globalmind_sim`
funciona (mismo `NameError`).

| Nombre del default | En `miu_constants.py` (64 líneas) |
|---|---|
| `K_kuramoto` | 0 ocurrencias |
| `dt_default` | 0 ocurrencias |
| `omega_mean` | 0 ocurrencias |
| `omega_std` | 0 ocurrencias |
| `eta_strength` | 0 ocurrencias |

`miu_constants.py` define 30 nombres públicos (constantes físicas c,
hbar, G, k_B, longitudes de Planck, `Phi_c = 0.7`, valores D_f,
parámetros de energía oscura, H0) — ninguno de los 5. Verificado
2026-11-09 ~07:48 -05, por grep y por `dir()` del módulo importado.

Precisión: el cuerpo de la simulación no es el problema. El único
nombre que el cuerpo necesita de las constantes, `D_f_mt = 2.5`, SÍ
está definido (línea 31: `p = dist**(-D_f_mt)`). Si la línea 21 no
fallara, el cuerpo podría correr. El archivo muere en la definición,
no en la ejecución.

## Comprobación

```bash
python3 kuramoto_roto_repro.py   # reproduce el NameError y el grep 0 en los 5 nombres
python3 test_kuramoto_roto.py    # 4 tests, reproducen la medición
```

Fuentes de la medición (solo lectura local, sin red, sin MIU vivo):
- `~/workspace/miu-verificacion-2026-11-06/extracted/MIU/Jaime393-MIU-a96abc3/src/globalmind_sim.py` — 70 líneas.
- `.../src/miu_constants.py` — 64 líneas.
- Plan: `~/workspace/mineria/PLAN_SIEMBRA_SEMILLA_LATENTE_2026-11-09.md` §2.

## Archivos

- `kuramoto_roto_repro.py` — reproducción mínima: la línea def tal cual
  + intento de import del archivo real, capturando el error.
- `test_kuramoto_roto.py` — 4 tests: NameError al definir, los 5
  nombres ausentes, NameError al importar, `D_f_mt` sí definido.
- `HUESO_KURAMOTO.md` — el hueso completo con sus límites.
- `EVOLUCION.md` — cambios entre versiones (v1: esta semilla).
- `CARENCIAS.md` — lo que NO se sabe; nunca es contenido.

---

ρ(x) > 0. Zvvvvv.
