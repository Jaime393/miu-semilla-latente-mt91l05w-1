#!/usr/bin/env python3
"""Reproduce el NameError de src/globalmind_sim.py (70 líneas).

El defecto está en la línea 21 del archivo real: los defaults de
run_simulation nombran 5 constantes que no existen en miu_constants.py.
Python evalúa los defaults al definir la función, así que el archivo
no se puede ni importar, ni ejecutar.

Verificado 2026-11-09 ~07:48 -05 contra:
  ~/workspace/miu-verificacion-2026-11-06/extracted/MIU/Jaime393-MIU-a96abc3/src/globalmind_sim.py
  ~/workspace/miu-verificacion-2026-11-06/extracted/MIU/Jaime393-MIU-a96abc3/src/miu_constants.py

Solo stdlib. No toca MIU vivo, no usa red, no lee claves.
"""

import os
import sys

# La línea def, copiada literal del archivo real (líneas 21-22).
DEF_LINE = (
    "def run_simulation(N=1000, K=K_kuramoto, dt=dt_default, T=30.0,\n"
    "                   omega_mean=omega_mean, omega_std=omega_std,\n"
    "                   eta=eta_strength):\n"
    "    pass\n"
)

FIVE_NAMES = ["K_kuramoto", "dt_default", "omega_mean", "omega_std",
              "eta_strength"]

SRC_DIR = os.path.expanduser(
    "~/workspace/miu-verificacion-2026-11-06/extracted/MIU/"
    "Jaime393-MIU-a96abc3/src")


def main():
    # 1. La línea def tal cual, sin nada definido antes.
    try:
        exec(DEF_LINE, {})
        print("1. def tal cual -> SIN ERROR (inesperado)")
    except NameError as exc:
        print(f"1. def tal cual -> NameError: {exc}")

    # 2. Los 5 nombres en miu_constants.py (grep 0 esperado en los 5).
    consts = os.path.join(SRC_DIR, "miu_constants.py")
    if os.path.exists(consts):
        with open(consts, encoding="utf-8") as fh:
            text = fh.read()
        for name in FIVE_NAMES:
            print(f"2. {name} en miu_constants.py: {text.count(name)}")
    else:
        print("2. miu_constants.py no encontrado en la ruta de verificación")

    # 3. Import del archivo real, si está presente.
    sim = os.path.join(SRC_DIR, "globalmind_sim.py")
    if os.path.exists(sim):
        sys.path.insert(0, SRC_DIR)
        try:
            import globalmind_sim  # noqa: F401
            print("3. import globalmind_sim -> SIN ERROR (inesperado)")
        except NameError as exc:
            print(f"3. import globalmind_sim -> NameError: {exc}")
        except ModuleNotFoundError as exc:
            print(f"3. import globalmind_sim -> ModuleNotFoundError: {exc} "
                  "(falta numpy/matplotlib, error distinto al medido)")
    else:
        print("3. globalmind_sim.py no encontrado en la ruta de verificación")


if __name__ == "__main__":
    main()
