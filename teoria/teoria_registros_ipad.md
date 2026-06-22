# Teoria Registros Ipad

Estas son las tablas que aparecen en tu captura:

ZCONTACTS

ZATTACHMENT

ZINTERACTIONS

ZKEYWORDS

ZVERSION

Z_1INTERACTIONS

Z_2INTERACTIONRECIPIENT

Z_3KEYWORDS

Z_METADATA

Z_MODELCACHE

Z_PRIMARYKEY

Aquí tienes la explicación clara:

Tabla

Descripción breve

ZCONTACTS

Lista de contactos con los que el usuario ha interactuado (números, emails, identificadores).

ZATTACHMENT

Metadatos de adjuntos asociados a interacciones (muy poco usado).

ZINTERACTIONS

La tabla principal: cada interacción registrada (llamada, mensaje, FaceTime, etc.).

ZKEYWORDS

Palabras clave asociadas a interacciones (para sugerencias de Siri/Spotlight).

ZVERSION

Versión del modelo CoreDuet. No contiene datos del usuario.

Z_1INTERACTIONS

Tabla puente entre contactos y sus interacciones.

Z_2INTERACTIONRECIPIENT

Tabla puente entre interacciones y destinatarios.

Z_3KEYWORDS

Tabla puente entre interacciones y palabras clave.

Z_METADATA

Metadatos de CoreData (versión del esquema).

Z_MODELCACHE

Caché interna del modelo de aprendizaje. No contiene datos útiles.

Z_PRIMARYKEY

Control interno de claves primarias. No contiene datos del usuario.

Estas son las que sí debes revisar:

Tabla

Por qué es importante

ZINTERACTIONS

Registra cada interacción del usuario con contactos. Es la tabla clave.

ZCONTACTS

Identifica a las personas con las que hubo interacción.

Z_1INTERACTIONS

Relaciona contactos ↔ interacciones.

Z_2INTERACTIONRECIPIENT

Relaciona interacciones ↔ destinatarios.

Estas tablas permiten reconstruir:

Con quién interactuó el usuario

Cuándo

Cuántas veces

Qué tipo de interacción fue

Aunque los mensajes/llamadas estén borrados

Aquí tienes la estructura relacional real:

Tabla origen

Relación

Tabla destino

Explicación

ZINTERACTIONS

1:N

Z_1INTERACTIONS

Cada interacción puede estar asociada a uno o varios contactos.

Z_1INTERACTIONS

N:1

ZCONTACTS

Permite saber con qué contacto se produjo la interacción.

ZINTERACTIONS

1:N

Z_2INTERACTIONRECIPIENT

Relaciona interacciones con destinatarios específicos.

Z_2INTERACTIONRECIPIENT

N:1

ZCONTACTS

Identifica al destinatario de la interacción.

ZINTERACTIONS

1:N

Z_3KEYWORDS

Palabras clave asociadas a la interacción.

Z_3KEYWORDS

N:1

ZKEYWORDS

Palabras clave usadas por Siri/Spotlight.

Ejemplos reales (sin inventar):

Fecha y hora de interacción

Tipo de interacción (call, sms, imessage, facetime)

Identificador del contacto

Frecuencia de interacción

Última vez que se interactuó

App usada (Phone, Messages, FaceTime)

Duración (si es llamada)

👉 Incluso si el usuario borró llamadas o mensajes, aquí puede quedar rastro.

Aquí tienes un texto profesional listo para copiar:

Se analizó la base de datos interactionC.db, ubicada en /private/var/mobile/Library/CoreDuet/People/. Esta base de datos pertenece al framework CoreDuet de iOS y registra metadatos de interacciones del usuario con contactos (llamadas, mensajes, FaceTime, etc.).

Aunque no almacena el contenido de las comunicaciones, sí conserva información sobre la existencia, frecuencia y tipo de interacción, incluso cuando los historiales de llamadas o mensajes han sido eliminados.

Las tablas relevantes para el análisis son ZINTERACTIONS, ZCONTACTS, Z_1INTERACTIONS y Z_2INTERACTIONRECIPIENT, que permiten reconstruir la actividad social del usuario.

Interpretar cada columna de ZINTERACTIONS

Ver si hay actividad aunque el resto del dispositivo esté “limpio”

Preparar una tabla final para tu informe

Explicar cómo correlacionarlo con llamadas y mensajes

Determinar si hubo borrado intencional