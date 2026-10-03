"""Genera shopify/productos.csv a partir de catalogo.py.

Uso:  python3 herramientas/generar_csv_shopify.py

El CSV sigue la plantilla oficial de Shopify (Productos > Importar).
Los productos se importan en estado "Draft": añade las fotos de tu
proveedor y actívalos cuando estén listos.
"""

import csv
from pathlib import Path

from catalogo import MARCA, PRODUCTOS

SALIDA = Path(__file__).resolve().parent.parent / "shopify" / "productos.csv"

COLUMNAS = [
    "Title", "URL handle", "Description", "Vendor", "Product category", "Type",
    "Tags", "Published on online store", "Status", "SKU", "Option1 name",
    "Option1 value", "Price", "Compare-at price", "Cost per item", "Charge tax",
    "Inventory tracker", "Continue selling when out of stock",
    "Weight value (grams)", "Weight unit for display", "Requires shipping",
    "Fulfillment service", "Gift card", "SEO title", "SEO description",
    "Google Shopping / Condition",
]


def euros(valor):
    return f"{valor:.2f}"


def sku(producto, variante=None):
    base = "SC-" + "".join(p[0] for p in producto["handle"].split("-")).upper()
    if variante:
        base += "-" + "".join(c for c in variante.upper() if c.isalnum())[:4]
    return base


def filas(producto):
    variantes = producto["variantes"] or [None]
    precios = producto.get("precio_por_variante", {})
    for i, variante in enumerate(variantes):
        fila = {
            "URL handle": producto["handle"],
            "SKU": sku(producto, variante),
            "Option1 value": variante or "Default Title",
            "Price": euros(precios.get(variante, producto["pvp"])),
            "Compare-at price": euros(producto["pvp_tachado"]) if producto["pvp_tachado"] else "",
            "Cost per item": euros(producto["coste"]),
            "Charge tax": "TRUE",
            # Sin seguimiento de stock: el inventario lo gestiona el proveedor.
            "Inventory tracker": "",
            "Continue selling when out of stock": "CONTINUE",
            "Weight value (grams)": producto["peso_g"],
            "Weight unit for display": "g",
            "Requires shipping": "TRUE",
            "Fulfillment service": "manual",
        }
        if i == 0:
            fila.update({
                "Title": producto["titulo"],
                "Description": producto["descripcion"].strip(),
                "Vendor": MARCA,
                "Product category": producto["categoria"],
                "Type": producto["tipo"],
                "Tags": ", ".join(producto["tags"]),
                "Published on online store": "TRUE",
                "Status": "Draft",
                "Option1 name": producto["opcion"] or "Title",
                "Gift card": "FALSE",
                "SEO title": producto["seo_titulo"],
                "SEO description": producto["seo_desc"],
                "Google Shopping / Condition": "New",
            })
        yield fila


def main():
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with SALIDA.open("w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUMNAS)
        escritor.writeheader()
        total = 0
        for producto in PRODUCTOS:
            for fila in filas(producto):
                escritor.writerow(fila)
                total += 1
    print(f"{SALIDA.relative_to(Path.cwd()) if SALIDA.is_relative_to(Path.cwd()) else SALIDA}: "
          f"{len(PRODUCTOS)} productos, {total} filas")


if __name__ == "__main__":
    main()
