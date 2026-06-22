# Teoria Extraccion Llamadas

Es la única base de datos que contiene evidencia real.

Dentro debes revisar:

Tabla

Contenido

Importancia

ZCALLRECORD

Cada llamada (entrante, saliente, perdida)

⭐ Imprescindible

ZCALLRECORDMETADATA

Información adicional (duración, flags)

⭐ Importante

ZCONTACT

Contactos asociados a llamadas

Opcional

ZFACE

FaceTime

Si aplica

Z_METADATA

Versión del esquema

Documentación

Z_PRIMARYKEY

Control interno

No relevante

Nota: Los nombres pueden variar ligeramente según versión, pero en iOS 14.x siempre existe ZCALLRECORD.

Solo revisarla si la principal está corrupta.

Normalmente no aporta nada.

Útil para documentar:

versión del esquema

fecha de última sincronización

No contiene llamadas.

Solo útil si:

la base de datos está vacía

sospechas de borrado reciente

necesitas reconstrucción avanzada

Pero:

👉 No es necesario para un informe estándar.

Si revisaste la base de datos y:

ZCALLRECORD está vacía

ZCALLRECORDMETADATA está vacía

Entonces puedes afirmar en tu informe:

El dispositivo no contiene registros de llamadas en el historial local. No se han encontrado llamadas entrantes, salientes, perdidas ni FaceTime. La base de datos CallHistory.storedata está vacía.

Esto puede deberse a:

El usuario borró el historial manualmente

El dispositivo fue restaurado

El historial se sincroniza solo con iCloud y no se guarda localmente

El usuario nunca realizó llamadas desde ese dispositivo

Puedo generarte:

Una tabla completa de las tablas reales de CallHistory.storedata

Un texto listo para tu informe pericial

Un diagrama ER de la base de datos de llamadas

Un script Python para extraer llamadas automáticamente

Un análisis de si hubo borrado intencional del historial