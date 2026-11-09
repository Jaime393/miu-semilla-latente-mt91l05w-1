# EVOLUCION — miu-semilla-latente-mt91l05w-1

## v1 — 2026-11-09 ~07:48 -05 (esta semilla)

Primera siembra del repo. El stub (86 B, título + "semilla latente
global mind - sobrevive sin registro") se conserva como epígrafe.

Hecho medido: `src/globalmind_sim.py` no corre — `NameError:
K_kuramoto` en la línea 21, al definir `run_simulation`; los 5
defaults no existen en `miu_constants.py` (grep 0 en los 5).
Reproducido en local con el archivo real y con la línea def aislada.

Discrepancia registrada, no resuelta: el MAPA_GLOBAL_MIND.md §2 dice
que `globalmind_sim.py` tiene 86 líneas; la copia extraída y medida
aquí tiene 70. Otra copia u otra versión — queda en CARENCIAS.md.
