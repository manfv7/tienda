# Catálogo de lanzamiento y precios

Nueve productos agrupados en los tres problemas que no dejan dormir en España: **calor, ruido y luz**. Los datos vienen de `herramientas/catalogo.py`. Si cambias algo, edítalo allí y vuelve a ejecutar:

```bash
python3 herramientas/generar_csv_shopify.py   # regenera shopify/productos.csv
python3 herramientas/calculadora.py --markdown # regenera la tabla de márgenes
```

## Productos y qué buscar en el proveedor

| # | Producto | Problema | Búsqueda en CJ / Syncee (en inglés) | Papel |
|---|---|---|---|---|
| 1 | Antifaz 3D Oscuridad Total | Luz | `3D contoured sleep mask` | ⭐ Producto gancho para anuncios |
| 2 | Funda de Almohada Efecto Frío | Calor | `cooling pillowcase Q-max` | ⭐ Estrella de mayo a septiembre |
| 3 | Máquina de Ruido Blanco Calma | Ruido | `white noise machine night light` | ⭐ Más vendido todo el año |
| 4 | Despertador Amanecer | Luz | `sunrise alarm clock wake up light` | Ticket alto, oct–mar |
| 5 | Almohada Cervical Ergonómica | Postura | `butterfly cervical memory foam pillow` | Ticket alto |
| 6 | Tapones Reutilizables Silencio | Ruido | `silicone sleep earplugs reusable case` | Venta cruzada |
| 7 | Cinta con Auriculares para Dormir | Ruido | `sleep headband bluetooth headphones` | Regalo |
| 8 | Difusor Nocturno con Luz Cálida | Rutina | `ultrasonic diffuser warm light` | Venta cruzada |
| 9 | Kit Noche Perfecta (1 + 2 + 6) | Todo | — (se monta con los productos 1, 2 y 6) | Sube el ticket medio |

**El kit:** en Shopify es un producto propio. Pide al proveedor que envíe los tres artículos en el mismo pedido (en CJ, con la opción de *bundle / combine order*). Si no puede, quita el kit hasta que encuentres cómo hacerlo.

## Márgenes estimados

Suposiciones: IVA 21 %, comisión de pago 2,9 % + 0,30 € (Shopify Payments plan Basic), 5 % de reserva para devoluciones e incidencias. **Los costes son estimaciones**: sustitúyelos por los reales de tu proveedor.

| Producto | Coste+envío | PVP | Multiplic. | CPA máx. | Margen | ROAS mín. |
|---|---:|---:|---:|---:|---:|---:|
| Antifaz 3D Oscuridad Total | 6.10 € | 19.90 € | x3.3 | 8.65 € | 53% | 2.30 |
| Funda de Almohada Efecto Frío | 9.50 € | 24.90 € | x2.6 | 9.03 € | 44% | 2.76 |
| Máquina de Ruido Blanco Calma | 12.50 € | 34.90 € | x2.8 | 13.59 € | 47% | 2.57 |
| Despertador Amanecer | 18.70 € | 49.90 € | x2.7 | 18.73 € | 45% | 2.66 |
| Almohada Cervical Ergonómica | 20.30 € | 54.90 € | x2.7 | 20.91 € | 46% | 2.63 |
| Tapones Reutilizables Silencio | 5.00 € | 17.90 € | x3.6 | 8.23 € | 56% | 2.17 |
| Cinta con Auriculares para Dormir | 10.20 € | 29.90 € | x2.9 | 12.11 € | 49% | 2.47 |
| Difusor Nocturno con Luz Cálida | 12.40 € | 32.90 € | x2.7 | 12.18 € | 45% | 2.70 |
| Kit Noche Perfecta | 15.90 € | 49.90 € | x3.1 | 21.53 € | 52% | 2.32 |

Cómo leer la tabla:

- **CPA máx.**: lo máximo que puedes pagar en anuncios por cada venta sin perder dinero. Si Meta te cobra 12 € por vender un antifaz, pierdes 3,35 €.
- **ROAS mín.**: el ROAS que tiene que darte la campaña para no perder dinero. Apunta a **ROAS ≥ 3** para ganar dinero de verdad.
- Los gastos fijos (plan de Shopify, apps, dominio) no están en la tabla: cúbrelos con el volumen.

## Reglas de precio

1. **Multiplica el coste (producto + envío) como mínimo por 2,5.** Por debajo, la publicidad se come el beneficio.
2. **Precios terminados en ,90.** Es lo habitual en España.
3. **Nada de precios tachados inventados.** La ley española (directiva Ómnibus) obliga a que el precio "antes" de una rebaja sea el más bajo que hayas aplicado en los 30 días anteriores. Si quieres hacer rebajas en el Black Friday, mantén el precio normal al menos 30 días antes.
4. **Envío gratis desde 35 €** y 3,95 € por debajo. Empuja a comprar dos productos o el kit.
5. **Venta cruzada en el carrito**: antifaz → tapones; ruido blanco → tapones; funda → antifaz. Usa la sección *Productos relacionados* de Dawn o *Shopify Search & Discovery* (gratis).

## Calendario de producto en España

| Meses | Qué empujar | Por qué |
|---|---|---|
| Ene–Feb | Despertador amanecer, almohada | Propósitos de año nuevo, días cortos |
| Mar–Abr | Antifaz | Cambio de hora (último domingo de marzo): amanece antes |
| May–Sep | **Funda efecto frío**, antifaz, ruido blanco | Noches tropicales, ventanas abiertas, ruido de terrazas |
| Oct | Despertador amanecer | Cambio de hora (último domingo de octubre): anochece antes |
| Nov–Dic | **Kit Noche Perfecta**, cinta con auriculares | Black Friday y Navidad: regalos |
