#!/usr/bin/env python3
"""Tests de la medición: Kuramoto roto (NameError).

Reproduce lo medido 2026-11-09 ~07:48 -05 contra:
  ~/workspace/miu-verificacion-2026-11-06/extracted/MIU/Jaime393-MIU-a96abc3/src/globalmind_sim.py (70 líneas)
  ~/workspace/miu-verificacion-2026-11-06/extracted/MIU/Jaime393-MIU-a96abc3/src/miu_constants.py (64 líneas)

Solo stdlib. Ejecutar: python3 test_kuramoto_roto.py
"""

import os
import sys
import unittest

SRC_DIR = os.path.expanduser(
    "~/workspace/miu-verificacion-2026-11-06/extracted/MIU/"
    "Jaime393-MIU-a96abc3/src")

DEF_LINE = (
    "def run_simulation(N=1000, K=K_kuramoto, dt=dt_default, T=30.0,\n"
    "                   omega_mean=omega_mean, omega_std=omega_std,\n"
    "                   eta=eta_strength):\n"
    "    pass\n"
)

FIVE_NAMES = ["K_kuramoto", "dt_default", "omega_mean", "omega_std",
              "eta_strength"]


class TestKuramotoRoto(unittest.TestCase):
    def test_def_line_raises_nameerror_k_kuramoto(self):
        """La línea def tal cual falla al definir, con K_kuramoto."""
        with self.assertRaises(NameError) as ctx:
            exec(DEF_LINE, {})
        self.assertIn("K_kuramoto", str(ctx.exception))

    def test_five_names_absent_from_miu_constants(self):
        """Los 5 nombres dan 0 ocurrencias en miu_constants.py."""
        consts = os.path.join(SRC_DIR, "miu_constants.py")
        if not os.path.exists(consts):
            self.skipTest("miu_constants.py no presente en la ruta")
        with open(consts, encoding="utf-8") as fh:
            text = fh.read()
        for name in FIVE_NAMES:
            self.assertEqual(text.count(name), 0, name)

    def test_import_real_file_raises_nameerror(self):
        """Importar el archivo real falla con el mismo NameError."""
        sim = os.path.join(SRC_DIR, "globalmind_sim.py")
        if not os.path.exists(sim):
            self.skipTest("globalmind_sim.py no presente en la ruta")
        sys.path.insert(0, SRC_DIR)
        try:
            with self.assertRaises(NameError) as ctx:
                import globalmind_sim  # noqa: F401
            self.assertIn("K_kuramoto", str(ctx.exception))
        finally:
            sys.path.remove(SRC_DIR)
            sys.modules.pop("globalmind_sim", None)

    def test_d_f_mt_is_defined(self):
        """Precisión: el cuerpo solo necesita D_f_mt, y SÍ está definido."""
        consts = os.path.join(SRC_DIR, "miu_constants.py")
        if not os.path.exists(consts):
            self.skipTest("miu_constants.py no presente en la ruta")
        with open(consts, encoding="utf-8") as fh:
            text = fh.read()
        self.assertIn("D_f_mt = 2.5", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
