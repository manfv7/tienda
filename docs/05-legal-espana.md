# Lo legal y fiscal para vender en España

> Esto es una guía práctica para ubicarte, **no asesoramiento legal ni fiscal**. Antes de facturar, habla con una gestoría (suelen cobrar 40–80 €/mes a un autónomo y te ahorran disgustos).

## 1. Darte de alta

- **Alta de autónomo** en la Seguridad Social (RETA) y en Hacienda (modelo 036/037), epígrafe de comercio al por menor por internet. La **tarifa plana** de nuevos autónomos reduce mucho la cuota los primeros 12 meses: pregunta a tu gestoría la cuantía actual.
- Si vas a vender de forma habitual, tienes que darte de alta aunque factures poco. "No llego al salario mínimo" **no** es una excepción válida para la cuota de autónomos.
- Más adelante, si factura bien, compara con montar una **SL**.

## 2. IVA

- Vendes a particulares en España: cobras **IVA del 21 %** (ya incluido en tus PVP).
- Declaras el IVA cada trimestre (modelo 303) y restas el IVA que te cobran tus proveedores de la UE si te facturan con IVA. Ojo: si un proveedor de otro país de la UE te factura **sin IVA** (operación intracomunitaria), necesitas estar en el **ROI** (Registro de Operadores Intracomunitarios). Pídeselo a tu gestoría desde el principio.
- Si en el futuro vendes a otros países de la UE y superas 10.000 €/año en esas ventas, te tocará el régimen **OSS** (ventanilla única).
- Por eso empezamos **solo con península y Baleares**: Canarias, Ceuta y Melilla tienen otros impuestos (IGIC, IPSI) y aduanas.

## 3. Páginas obligatorias en la tienda

| Página | Ley | En el repo |
|---|---|---|
| Aviso legal (quién eres: nombre, NIF, dirección, email) | LSSI, art. 10 | `shopify/paginas/aviso-legal.html` |
| Política de privacidad | RGPD + LOPDGDD | Generador de Shopify, adaptado |
| Política de cookies + banner | LSSI art. 22 + RGPD | Banner de Shopify (Privacidad del cliente) |
| Condiciones de venta (términos) | Ley General de Consumidores | Generador de Shopify, adaptado |
| Envíos | Consumidores (plazos y costes antes de pagar) | `shopify/paginas/politica-envios.html` |
| Devoluciones y desistimiento + formulario | Consumidores, arts. 102–108 | `shopify/paginas/politica-devoluciones.html` |

## 4. Derechos del cliente que tienes que respetar

- **Desistimiento de 14 días naturales** desde que recibe el producto, sin dar explicaciones. Le devuelves el dinero (incluido el envío estándar) en 14 días como máximo. Puedes hacer que pague él el envío de vuelta **si se lo avisas antes de la compra** (así está en nuestra política).
- **Excepción de higiene**: los productos precintados que, por higiene, no se pueden devolver una vez abiertos (en nuestro catálogo, los **tapones**) quedan excluidos si se han desprecintado. Debe constar claramente en la ficha y en la política.
- **Garantía legal de 3 años** en productos nuevos (desde 2022). Si el producto sale defectuoso, respondes tú, no el proveedor. Negocia con el proveedor que te cubra a ti.
- **Precios con IVA incluido** y gastos de envío visibles antes de pagar.
- **Rebajas**: el precio "antes" tiene que ser el más bajo de los últimos 30 días (directiva Ómnibus).
- **Reclamaciones**: informa de un email y una dirección donde reclamar. Las normas sobre hojas de reclamaciones online cambian según la comunidad autónoma: confírmalo con tu gestoría.

## 5. Productos

- Comprueba que todo lo eléctrico (ruido blanco, despertador, difusor, cinta Bluetooth) lleve **marcado CE** y manual en español. Pide al proveedor la declaración de conformidad. Como importas y vendes con tu marca, frente al cliente el responsable eres tú.
- Nada de cosméticos, suplementos ni productos sanitarios sin los registros correspondientes (ver `docs/01-estudio-de-nicho.md`, apartado 4).
- Si vendes aparatos eléctricos, infórmate sobre el registro de productores de **RAEE** y de **envases** (los dos son obligaciones de responsabilidad ampliada del productor). Tu gestoría o el propio proveedor te pueden orientar.
