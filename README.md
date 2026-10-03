# Siesta & Co. — tienda de dropshipping en Shopify

Tienda online de **productos para dormir mejor**, para el mercado español. Enfoque: los tres enemigos del sueño en España, **calor, ruido y luz**.

## Por qué este nicho

El 48 % de los adultos en España no duerme bien (Sociedad Española de Neurología), el mercado del sueño crece en torno a un 5–6 % anual y casi no hay tiendas de marca especializadas en español. Los productos son ligeros, no tienen tallas y aguantan márgenes de ×2,6–3,6. Estudio completo con fuentes y la matriz de puntuación: [`docs/01-estudio-de-nicho.md`](docs/01-estudio-de-nicho.md).

## Contenido del repositorio

| Ruta | Qué es |
|---|---|
| [`docs/01-estudio-de-nicho.md`](docs/01-estudio-de-nicho.md) | Comparativa de 8 nichos, por qué gana *sueño*, qué no vender y cómo validarlo |
| [`docs/02-guia-montaje-shopify.md`](docs/02-guia-montaje-shopify.md) | Paso a paso: cuenta, ajustes, pagos, proveedor, tema, apps y checklist |
| [`docs/03-catalogo-y-precios.md`](docs/03-catalogo-y-precios.md) | Los 9 productos, qué buscar en el proveedor, márgenes y calendario |
| [`docs/04-plan-de-lanzamiento.md`](docs/04-plan-de-lanzamiento.md) | Primeros 60 días: contenido orgánico, test de anuncios, emails y KPI |
| [`docs/05-legal-espana.md`](docs/05-legal-espana.md) | Autónomo, IVA, páginas obligatorias y derechos del consumidor |
| [`shopify/productos.csv`](shopify/productos.csv) | Catálogo listo para *Productos › Importar* (entra como borrador) |
| [`shopify/paginas/`](shopify/paginas/) | Textos de las páginas y políticas (rellena los `[CORCHETES]`) |
| [`shopify/theme/`](shopify/theme/) | Secciones a medida para el tema Dawn |
| [`herramientas/`](herramientas/) | Catálogo en Python, generador del CSV y calculadora de márgenes |

## Herramientas

```bash
# Regenerar el CSV de Shopify después de editar herramientas/catalogo.py
python3 herramientas/generar_csv_shopify.py

# Tabla de márgenes, CPA máximo y ROAS mínimo de todo el catálogo
python3 herramientas/calculadora.py

# Calcular un producto suelto (coste y envío del proveedor, PVP con IVA)
python3 herramientas/calculadora.py --coste 5 --envio 3 --pvp 24.90
```

Solo necesitan Python 3.9 o posterior, sin dependencias.

## Por dónde empezar

1. Lee el estudio de nicho y haz la validación del apartado 5 (una tarde).
2. Sigue la guía de montaje.
3. Pide muestras, cambia los costes estimados por los reales y vuelve a ejecutar la calculadora.
4. Lanza con el plan de 60 días.

> Los costes de proveedor son **estimaciones**. Los textos legales son **plantillas**: revísalos con una gestoría antes de abrir.
