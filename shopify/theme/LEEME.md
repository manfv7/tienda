# Secciones a medida para el tema Dawn

Dos secciones para la portada, pensadas para **Dawn 12 o posterior** (usan esquemas de color). Validadas con Shopify Theme Check.

| Archivo | Qué es |
|---|---|
| `sections/sc-barra-confianza.liquid` | Barra con 4 garantías: envío gratis, 30 días, pago seguro, probado por nosotros |
| `sections/sc-problemas.liquid` | Bloque "¿Qué no te deja dormir?": tarjetas Calor / Ruido / Luz que enlazan a cada colección |
| `assets/siesta-co.css` | Estilos de las dos secciones |

## Cómo instalarlas

1. Tienda online › Temas › en Dawn, menú `···` › **Editar código**.
2. Carpeta **Sections** › *Añadir una nueva sección* › nombre `sc-barra-confianza` › borra lo que trae y pega el contenido del archivo. Repite con `sc-problemas`.
3. Carpeta **Assets** › *Añadir un nuevo recurso* › *Crear un archivo en blanco* › `siesta-co.css` › pega el contenido.
4. Guarda, sal a **Personalizar** › *Añadir sección* › aparecen como **SC · Barra de confianza** y **SC · Calor, ruido, luz**.
5. En cada tarjeta de *Calor, ruido, luz* elige su colección (*Contra el calor*, *Contra el ruido*, *Contra la luz*). Cuando tengas fotos propias, súbelas: sustituyen al emoji.

Alternativa con terminal: si usas [Shopify CLI](https://shopify.dev/docs/storefronts/themes/tools/cli), descarga el tema con `shopify theme pull`, copia estas carpetas encima y súbelo con `shopify theme push`.
