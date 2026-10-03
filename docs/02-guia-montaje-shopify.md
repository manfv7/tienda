# Guía de montaje en Shopify, paso a paso

Tiempo estimado: **un fin de semana**. Sigue el orden: cada paso depende del anterior.

## 0. Antes de empezar (30 min)

- [ ] Comprueba que el nombre está libre: dominio (`siestaco.es` / `siestaand.co` / `siesta-co.com`), Instagram y TikTok `@siestaco`. Si está pillado, alternativas: *Siestea*, *Bruma Sleep*, *Nubo Descanso*.
- [ ] Busca la marca en la [OEPM](https://www.oepm.es/) para no pisar una marca registrada.
- [ ] Crea un email de la tienda (p. ej. `hola@tudominio`).

## 1. Crear la tienda

1. Regístrate en [shopify.com/es](https://www.shopify.com/es). Ahora mismo hay **3 días gratis y luego 1 €/mes durante 3 meses**.
2. País: **España**. Moneda: **EUR**. Idioma de la tienda: **español**.
3. Cuando acabe la prueba, el plan **Basic** (39 €/mes, o 29 €/mes con pago anual) es suficiente hasta facturar varios miles al mes.

## 2. Ajustes básicos (Configuración)

| Dónde | Qué poner |
|---|---|
| Configuración › Tienda | Nombre *Siesta & Co.*, email de contacto, dirección fiscal (obligatoria por ley) |
| Configuración › Mercados | Solo **España**. Excluye Canarias, Ceuta y Melilla al principio (IGIC y aduanas complican los envíos) |
| Configuración › Impuestos y aranceles | Activa **"Todos los precios incluyen impuestos"**. IVA España 21 % |
| Configuración › Envío y entrega | Tarifa *Estándar (2–5 días laborables)*: **3,95 €**. Tarifa *Gratis*: **0 € con pedidos ≥ 35 €** |
| Configuración › Notificaciones | Revisa que los emails estén en español y pon el logo |
| Configuración › Idiomas | Español como predeterminado |

> **¿Por qué 35 €?** El ticket de un solo producto suele estar entre 18 y 30 €. Con 35 € el cliente añade un segundo producto o se lleva el *Kit Noche Perfecta* (49,90 €). Sube el ticket medio sin coste extra para ti.

## 3. Pagos

1. **Shopify Payments**: tarjeta, Apple Pay y Google Pay. Actívalo primero (es la pasarela con menos comisiones dentro de Shopify).
2. **PayPal**: actívalo; da confianza al comprador español.
3. **Bizum**: busca "Bizum" en la App Store de Shopify (hay apps que lo conectan vía Redsys/tu banco). Muy recomendable en España; añádelo cuando tengas las primeras ventas.
4. **Contra reembolso**: **no** al principio. En dropshipping genera muchos pedidos rechazados que tú pagas.

## 4. Proveedor (lo más importante)

Requisito innegociable: **almacén en la UE, entrega en España en 2–5 días**. El cliente español no espera 3 semanas a un envío desde China, y esos pedidos acaban en reclamaciones y devoluciones.

| Proveedor | Para qué | Cómo se conecta |
|---|---|---|
| **CJ Dropshipping** | La mayor parte del catálogo. Filtra por *Warehouse: EU/ES/DE* | App "CJ Dropshipping" en Shopify |
| **BigBuy** | Proveedor español, envío 1–5 días; buena alternativa si CJ no tiene stock UE | App "BigBuy" (plan de pago) |
| **Syncee** | Proveedores europeos varios; útil para la almohada y el despertador | App "Syncee" |
| **Dropea** | Catálogo con stock en España y Portugal | App "dropea" |

Pasos:

1. Instala la app del proveedor.
2. Pide **muestras** de los 3 productos estrella (antifaz, funda, ruido blanco). Pruébalos tú: grabarás con ellos los anuncios.
3. Busca cada producto por las palabras clave de la tabla de `docs/03-catalogo-y-precios.md`.
4. **Conecta** cada producto del proveedor con el producto ya importado (opción *Connect / Map to existing product*), variante por variante.
5. Actualiza el coste real en `herramientas/catalogo.py` y vuelve a ejecutar la calculadora.

## 5. Importar los productos

1. Productos › **Importar** › sube `shopify/productos.csv`.
2. Se crean los 9 productos en estado **Borrador**.
3. En cada uno: añade fotos (las del proveedor + las tuyas con las muestras), revisa el texto y pasa el estado a **Activo**.
4. Crea las **colecciones** (Productos › Colecciones), automáticas por etiqueta:

| Colección | Condición | Para |
|---|---|---|
| Contra el calor | Etiqueta = `calor` | Funda efecto frío |
| Contra el ruido | Etiqueta = `ruido` | Ruido blanco, tapones |
| Contra la luz | Etiqueta = `luz` | Antifaz, despertador |
| Más vendidos | Etiqueta = `bestseller` | Portada |
| Ideas para regalar | Etiqueta = `regalo` | Campañas de Navidad |

## 6. Tema y diseño

1. Tienda online › Temas › usa **Dawn** (gratuito, rápido y fiable).
2. **Colores** (Personalizar › Configuración del tema › Colores):
   - Fondo: `#F7F3EE` (crema) · Texto: `#1F2A44` (azul noche) · Botones: `#1F2A44` con texto `#F7F3EE` · Acento: `#C9A27E` (arena).
3. **Tipografía**: títulos *Fraunces* o *DM Serif Display*, texto *Inter*.
4. Añade nuestras secciones a medida (ver `shopify/theme/LEEME.md`): barra de confianza y bloque "¿Qué no te deja dormir?".
5. Estructura de la portada:
   1. Banner con imagen: *"Duerme como en la siesta de agosto. Pero de noche."* + botón *Descubre cómo*.
   2. **Barra de confianza** (sección propia).
   3. **¿Qué no te deja dormir? Calor / Ruido / Luz** (sección propia) → colecciones.
   4. Colección destacada: *Más vendidos*.
   5. Banner del *Kit Noche Perfecta*.
   6. Reseñas (cuando las tengas).
   7. Preguntas frecuentes (sección "Contenido desplegable" de Dawn).
   8. Suscripción a la newsletter: *"−10 % en tu primer pedido"*.

## 7. Páginas y políticas

1. Tienda online › Páginas › *Añadir página*. Para `sobre-nosotros`, `preguntas-frecuentes`, `contacto` y `aviso-legal`, pega el contenido en la vista HTML (`<>`) del editor. A *Contacto* asígnale la plantilla `page.contact` para que muestre el formulario.
2. Configuración › **Políticas**: pega `politica-devoluciones.html` y `politica-envios.html`. Para *Privacidad* y *Términos del servicio* usa el generador de Shopify y adáptalo. Rellena todos los datos entre `[corchetes]`.
3. Menú principal: *Inicio · Calor · Ruido · Luz · Packs · Ayuda*. Menú del pie: *Sobre nosotros · Envíos · Devoluciones · Preguntas frecuentes · Contacto · Aviso legal · Privacidad · Términos*.

## 8. Apps (todas con plan gratis para empezar)

| App | Para qué |
|---|---|
| **Judge.me** | Reseñas con foto. Pide reseña por email a los 10 días |
| **Shopify Email** o **Klaviyo** | Carrito abandonado, bienvenida, posventa |
| **Shopify Inbox** | Chat con clientes |
| Banner de cookies de Shopify (*Privacidad del cliente*) | Obligatorio en la UE; actívalo en Configuración › Privacidad del cliente |

No instales más de lo necesario: cada app ralentiza la tienda.

## 9. Checklist antes de abrir

- [ ] Dominio propio conectado (Configuración › Dominios).
- [ ] Todos los productos con 5+ fotos y al menos 1 vídeo corto.
- [ ] **Pedido de prueba real** con tu tarjeta: compra, comprueba que llega al proveedor, recibe el paquete, haz la devolución.
- [ ] Emails de confirmación y envío en español y con tu logo.
- [ ] Páginas legales completas, sin `[corchetes]` pendientes.
- [ ] Tienda probada en el móvil (el 80 % del tráfico vendrá de ahí).
- [ ] Velocidad: Tienda online › Temas › informe de velocidad.
- [ ] Píxel de Meta y de TikTok instalados (apps "Facebook & Instagram" y "TikTok").
- [ ] Quita la contraseña de la tienda (Tienda online › Preferencias).

Siguiente paso: `docs/04-plan-de-lanzamiento.md`.
