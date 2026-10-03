"""Calculadora de márgenes para dropshipping en España.

Uso:
  python3 herramientas/calculadora.py                 # tabla del catálogo
  python3 herramientas/calculadora.py --markdown      # tabla en Markdown
  python3 herramientas/calculadora.py --coste 5 --envio 3 --pvp 24.90

Qué calcula, por pedido de una unidad:
  ingreso neto  = PVP sin IVA
  contribución  = ingreso neto - coste - envío - comisión de pago - reserva devoluciones
  CPA máximo    = contribución (lo máximo que puedes pagar en anuncios por venta sin perder)
  ROAS mínimo   = PVP / contribución (ROAS que te marca Meta/TikTok para no perder dinero)

Ajusta las SUPOSICIONES a tu caso: plan de Shopify, pasarela y proveedor reales.
"""

import argparse

from catalogo import PRODUCTOS

SUPOSICIONES = {
    "iva": 0.21,               # IVA general España (península y Baleares)
    "comision_pct": 0.029,     # Shopify Payments plan Basic (comprueba tu tarifa)
    "comision_fija": 0.30,     # EUR por transacción
    "reserva_devoluciones": 0.05,  # % del ingreso neto apartado para devoluciones/incidencias
}


def calcular(coste, envio, pvp, s=SUPOSICIONES):
    neto = pvp / (1 + s["iva"])
    comision = pvp * s["comision_pct"] + s["comision_fija"]
    reserva = neto * s["reserva_devoluciones"]
    contribucion = neto - coste - envio - comision - reserva
    return {
        "neto": neto,
        "contribucion": contribucion,
        "margen_pct": contribucion / neto if neto else 0,
        "cpa_max": contribucion,
        "roas_min": pvp / contribucion if contribucion > 0 else float("inf"),
        "multiplicador": pvp / (coste + envio),
    }


def fila(nombre, coste, envio, pvp):
    r = calcular(coste, envio, pvp)
    return [
        nombre, f"{coste + envio:.2f} €", f"{pvp:.2f} €", f"x{r['multiplicador']:.1f}",
        f"{r['contribucion']:.2f} €", f"{r['margen_pct']:.0%}", f"{r['roas_min']:.2f}",
    ]


CABECERA = ["Producto", "Coste+envío", "PVP", "Multiplic.", "CPA máx.", "Margen", "ROAS mín."]


def imprimir(filas, markdown):
    if markdown:
        print("| " + " | ".join(CABECERA) + " |")
        print("|" + "|".join(["---"] + ["---:"] * (len(CABECERA) - 1)) + "|")
        for f in filas:
            print("| " + " | ".join(f) + " |")
        return
    anchos = [max(len(str(x)) for x in col) for col in zip(CABECERA, *filas)]
    for f in [CABECERA, *filas]:
        print("  ".join(str(x).ljust(a) for x, a in zip(f, anchos)))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--coste", type=float, help="coste del producto (EUR, sin IVA)")
    p.add_argument("--envio", type=float, default=0.0, help="coste de envío del proveedor (EUR)")
    p.add_argument("--pvp", type=float, help="precio de venta con IVA (EUR)")
    p.add_argument("--markdown", action="store_true", help="salida en tabla Markdown")
    a = p.parse_args()

    if a.coste is not None or a.pvp is not None:
        if a.coste is None or a.pvp is None:
            p.error("--coste y --pvp van juntos")
        filas = [fila("Producto", a.coste, a.envio, a.pvp)]
    else:
        filas = [fila(x["titulo"], x["coste"], x["envio"], x["pvp"]) for x in PRODUCTOS]
    imprimir(filas, a.markdown)


if __name__ == "__main__":
    main()
