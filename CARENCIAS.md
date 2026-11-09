# CARENCIAS — miu-semilla-latente-mt91l05w-1

Lo que NO se sabe va aquí, nunca en la semilla. Cada ítem lleva dónde
se buscó (o que no se buscó) y fecha.

- **NO SÉ — qué valores deberían tener los 5 defaults.**
  `K_kuramoto`, `dt_default`, `omega_mean`, `omega_std`,
  `eta_strength` no existen en `miu_constants.py` (grep 0,
  2026-11-09 ~07:48 -05). Ningún archivo leído les da valor. El
  `__main__` del propio archivo pasa `dt=0.01` y `eta=0.1` al llamar,
  pero no `K`, `omega_mean` ni `omega_std` — tampoco dice qué valores
  se pretendían.
- **NO SÉ — dónde está la copia de 86 líneas.**
  El MAPA_GLOBAL_MIND.md §2 dice que `globalmind_sim.py` tiene 86
  líneas; la copia extraída en
  `~/workspace/miu-verificacion-2026-11-06/extracted/MIU/Jaime393-MIU-a96abc3/src/`
  mide 70 (medido 2026-11-09 ~07:48 -05). Otra copia u otra versión,
  sin localizar. No se buscó fuera de esa ruta.
- **NO SÉ — si la simulación corrió alguna vez con éxito.**
  No hay logs, resultados ni figuras del archivo en los materiales
  leídos (2026-11-09). El `__main__` guarda `globalmind_transition.png`
  y dibuja la figura, pero ningún PNG acompaña a la copia medida.
- **NO SÉ — si existe una versión corregida en otra rama o repo.**
  Solo se leyó `main` de la copia extraída (2026-11-09). Otras ramas
  no se verificaron.
- **NO SÉ — por qué faltan los 5 nombres.**
  Pudo ser un olvido, un refactor incompleto o constantes que vivían
  en otro archivo. No hay commit ni comentario que lo explique en lo
  leído (2026-11-09). No se conjetura.
