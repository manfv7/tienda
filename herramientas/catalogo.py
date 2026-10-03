"""Catálogo de lanzamiento de Siesta & Co.

Fuente única de verdad: de aquí salen el CSV de importación de Shopify
(generar_csv_shopify.py) y la tabla de márgenes (calculadora.py).

Los costes son ESTIMACIONES de proveedor con almacén en la UE (CJ, BigBuy,
Syncee...). Antes de lanzar, sustitúyelos por el precio real que te dé tu
proveedor y vuelve a ejecutar los scripts.

Campos de cada producto:
  coste       -> precio del producto al proveedor (EUR, sin IVA)
  envio       -> lo que te cobra el proveedor por enviarlo a España (EUR)
  pvp         -> precio de venta al público, IVA incluido (EUR)
  pvp_tachado -> precio "antes" que se muestra tachado (o None)

OJO con pvp_tachado: en España una rebaja debe anunciarse respecto al precio
más bajo aplicado en los 30 días anteriores (directiva Ómnibus). No inventes
precios "antes". Solo el kit lleva tachado: es la suma real de sus productos.
"""

MARCA = "Siesta & Co."

PRODUCTOS = [
    {
        "handle": "antifaz-3d-oscuridad-total",
        "titulo": "Antifaz 3D Oscuridad Total",
        "tipo": "Antifaces",
        "categoria": "Health & Beauty > Personal Care > Sleeping Aids > Sleep Masks",
        "tags": ["antifaz", "luz", "viaje", "bestseller"],
        "peso_g": 60,
        "coste": 3.20,
        "envio": 2.90,
        "pvp": 19.90,
        "pvp_tachado": None,
        "opcion": "Color",
        "variantes": ["Negro", "Gris piedra", "Rosa palo"],
        "seo_titulo": "Antifaz para dormir 3D que bloquea el 100% de la luz | Siesta & Co.",
        "seo_desc": "Antifaz contorneado que no presiona los ojos ni despeina las pestañas. Oscuridad total para dormir, hacer la siesta o viajar. Envío gratis desde 35 €.",
        "descripcion": """
<p><strong>Oscuridad total sin presión en los ojos.</strong> Su forma 3D deja un hueco para cada ojo, así puedes parpadear con normalidad y no se arruina el rímel ni las extensiones.</p>
<ul>
<li>Bloquea la luz de farolas, persianas que no cierran y del amanecer de verano.</li>
<li>Espuma con memoria ligera (60 g): ni la notas.</li>
<li>Cinta ajustable que no tira del pelo.</li>
<li>Perfecto para la siesta, el avión o el turno de noche.</li>
</ul>
<p><em>Incluye bolsita de viaje.</em></p>
""",
    },
    {
        "handle": "funda-almohada-efecto-frio",
        "titulo": "Funda de Almohada Efecto Frío",
        "tipo": "Ropa de cama",
        "categoria": "Home & Garden > Linens & Bedding > Bedding > Pillowcases & Shams",
        "tags": ["calor", "verano", "almohada", "bestseller"],
        "peso_g": 180,
        "coste": 6.10,
        "envio": 3.40,
        "pvp": 24.90,
        "pvp_tachado": None,
        "opcion": "Medida",
        "variantes": ["75 cm", "90 cm"],
        "precio_por_variante": {"90 cm": 27.90},
        "seo_titulo": "Funda de almohada refrescante para noches de calor | Siesta & Co.",
        "seo_desc": "Tejido de enfriamiento que se nota fresco al tacto y disipa el calor de la cara. Para las noches tropicales de verano. Lavable a máquina.",
        "descripcion": """
<p><strong>Para las noches en las que no baja de 25 °C.</strong> Tejido de fibra refrescante que se siente frío al tacto y evacua el calor, en lugar de acumularlo como el algodón.</p>
<ul>
<li>Cara fría + cara de algodón para invierno: úsala todo el año.</li>
<li>Cremallera oculta, se adapta a almohadas estándar españolas.</li>
<li>Lavable a máquina a 30 °C.</li>
</ul>
""",
    },
    {
        "handle": "maquina-ruido-blanco",
        "titulo": "Máquina de Ruido Blanco Calma",
        "tipo": "Sonido",
        "categoria": "Health & Beauty > Personal Care > Sleeping Aids > White Noise Machines",
        "tags": ["ruido", "bebe", "vecinos", "bestseller"],
        "peso_g": 280,
        "coste": 8.90,
        "envio": 3.60,
        "pvp": 34.90,
        "pvp_tachado": None,
        "opcion": None,
        "variantes": [],
        "seo_titulo": "Máquina de ruido blanco para dormir: tapa vecinos y tráfico | Siesta & Co.",
        "seo_desc": "30 sonidos sin bucles (ruido blanco, rosa, lluvia, ventilador), temporizador y luz nocturna. Ideal para dormir con ruido de calle o para bebés.",
        "descripcion": """
<p><strong>El vecino de arriba, las motos, el camión de la basura… tapados.</strong> Un sonido constante y suave enmascara los ruidos que te despiertan.</p>
<ul>
<li>30 sonidos sin cortes: ruido blanco, rosa, marrón, lluvia, ventilador, olas.</li>
<li>Temporizador de 30/60/90 min o toda la noche.</li>
<li>Luz nocturna cálida regulable.</li>
<li>Carga USB-C y memoria del último sonido.</li>
</ul>
""",
    },
    {
        "handle": "despertador-simulador-amanecer",
        "titulo": "Despertador Amanecer",
        "tipo": "Despertadores",
        "categoria": "Home & Garden > Decor > Clocks > Alarm Clocks",
        "tags": ["despertar", "luz", "invierno"],
        "peso_g": 450,
        "coste": 14.50,
        "envio": 4.20,
        "pvp": 49.90,
        "pvp_tachado": None,
        "opcion": None,
        "variantes": [],
        "seo_titulo": "Despertador con simulación de amanecer y radio | Siesta & Co.",
        "seo_desc": "Te despierta con luz que aumenta poco a poco durante 30 minutos, como un amanecer real. Modo atardecer para dormirte, sonidos naturales y radio FM.",
        "descripcion": """
<p><strong>Despertarte sin sobresaltos, incluso en pleno invierno.</strong> La luz sube poco a poco durante los 30 minutos previos a tu alarma, como un amanecer.</p>
<ul>
<li>Modo atardecer: la luz baja lentamente para ayudarte a desconectar.</li>
<li>7 sonidos naturales + radio FM.</li>
<li>20 niveles de brillo y lámpara de lectura.</li>
</ul>
""",
    },
    {
        "handle": "almohada-cervical-ergonomica",
        "titulo": "Almohada Cervical Ergonómica",
        "tipo": "Almohadas",
        "categoria": "Home & Garden > Linens & Bedding > Bedding > Pillows",
        "tags": ["cuello", "postura", "almohada"],
        "peso_g": 1300,
        "coste": 13.80,
        "envio": 6.50,
        "pvp": 54.90,
        "pvp_tachado": None,
        "opcion": None,
        "variantes": [],
        "seo_titulo": "Almohada cervical viscoelástica ergonómica | Siesta & Co.",
        "seo_desc": "Almohada de espuma viscoelástica con forma de mariposa que sujeta cuello y cabeza, tanto si duermes de lado como boca arriba. Funda lavable.",
        "descripcion": """
<p><strong>Para quien se levanta con el cuello cargado.</strong> Forma de mariposa con dos alturas: elige la que mejor encaje con tu postura.</p>
<ul>
<li>Espuma viscoelástica que recupera la forma.</li>
<li>Hueco central para dormir boca arriba, laterales elevados para dormir de lado.</li>
<li>Funda transpirable, extraíble y lavable.</li>
</ul>
<p><em>Producto de confort. No es un producto sanitario.</em></p>
""",
    },
    {
        "handle": "tapones-silicona-dormir",
        "titulo": "Tapones Reutilizables Silencio",
        "tipo": "Tapones",
        "categoria": "Health & Beauty > Personal Care > Ear Care > Ear Plugs",
        "tags": ["ruido", "ronquidos", "viaje"],
        "peso_g": 30,
        "coste": 2.40,
        "envio": 2.60,
        "pvp": 17.90,
        "pvp_tachado": None,
        "opcion": "Color",
        "variantes": ["Negro", "Blanco", "Salvia"],
        "seo_titulo": "Tapones para dormir de silicona reutilizables | Siesta & Co.",
        "seo_desc": "Tapones de silicona suave con 4 tallas de almohadilla. Cómodos para dormir de lado. Ideales contra ronquidos y ruido. Con estuche.",
        "descripcion": """
<p><strong>Los ronquidos de tu pareja ya no son tu problema.</strong> Silicona suave que no aprieta, incluso si duermes de lado.</p>
<ul>
<li>4 tallas de almohadilla (XS-L) incluidas.</li>
<li>Reutilizables y lavables con agua y jabón.</li>
<li>Estuche magnético de bolsillo.</li>
</ul>
""",
    },
    {
        "handle": "cinta-auriculares-dormir",
        "titulo": "Cinta con Auriculares para Dormir",
        "tipo": "Sonido",
        "categoria": "Electronics > Audio > Audio Components > Headphones & Headsets > Headphones",
        "tags": ["musica", "podcast", "bluetooth", "regalo"],
        "peso_g": 70,
        "coste": 7.20,
        "envio": 3.00,
        "pvp": 29.90,
        "pvp_tachado": None,
        "opcion": "Color",
        "variantes": ["Gris", "Negro"],
        "seo_titulo": "Banda con auriculares Bluetooth para dormir de lado | Siesta & Co.",
        "seo_desc": "Auriculares planos integrados en una cinta suave. Escucha podcasts, meditaciones o ruido blanco sin que te molesten al dormir de lado.",
        "descripcion": """
<p><strong>Podcast o meditación sin cascos que se clavan.</strong> Altavoces ultraplanos dentro de una cinta elástica y transpirable.</p>
<ul>
<li>Bluetooth 5.x, hasta 10 h de batería.</li>
<li>Cómoda para dormir de lado.</li>
<li>Los altavoces se sacan para lavar la cinta.</li>
</ul>
""",
    },
    {
        "handle": "difusor-aromas-luz-calida",
        "titulo": "Difusor Nocturno con Luz Cálida",
        "tipo": "Ambiente",
        "categoria": "Home & Garden > Decor > Home Fragrance Accessories > Essential Oil Diffusers",
        "tags": ["ambiente", "rutina", "regalo"],
        "peso_g": 320,
        "coste": 8.60,
        "envio": 3.80,
        "pvp": 32.90,
        "pvp_tachado": None,
        "opcion": None,
        "variantes": [],
        "seo_titulo": "Difusor de aromas silencioso con luz cálida | Siesta & Co.",
        "seo_desc": "Difusor ultrasónico silencioso con luz ámbar regulable y apagado automático. Crea tu ritual de desconexión antes de dormir.",
        "descripcion": """
<p><strong>Tu ritual para desconectar antes de dormir.</strong> Ultrasónico y silencioso, con luz ámbar que no te despeja como la luz blanca.</p>
<ul>
<li>Depósito de 300 ml: hasta 8 h.</li>
<li>Apagado automático sin agua.</li>
<li>Temporizador de 1/3/6 h.</li>
</ul>
<p><em>Aceites esenciales no incluidos.</em></p>
""",
    },
    {
        "handle": "kit-noche-perfecta",
        "titulo": "Kit Noche Perfecta",
        "tipo": "Packs",
        "categoria": "Health & Beauty > Personal Care > Sleeping Aids",
        "tags": ["pack", "regalo", "bestseller"],
        "peso_g": 270,
        # antifaz + tapones + funda 75 cm, mismo envío consolidado
        "coste": 3.20 + 2.40 + 6.10,
        "envio": 4.20,
        "pvp": 49.90,
        "pvp_tachado": 62.70,
        "opcion": None,
        "variantes": [],
        "seo_titulo": "Kit para dormir: antifaz 3D + tapones + funda fresca | Siesta & Co.",
        "seo_desc": "Todo lo que necesitas para dormir sin luz, sin ruido y sin calor. Antifaz 3D, tapones reutilizables y funda de almohada efecto frío. Ahorra un 20%.",
        "descripcion": """
<p><strong>Sin luz, sin ruido, sin calor.</strong> Nuestros tres más vendidos juntos: ahorras un 20 % frente a comprarlos por separado.</p>
<ul>
<li>1 × Antifaz 3D Oscuridad Total (negro)</li>
<li>1 × Tapones Reutilizables Silencio (negro)</li>
<li>1 × Funda de Almohada Efecto Frío (75 cm)</li>
</ul>
<p>Perfecto para regalar (o regalarte).</p>
""",
    },
]
