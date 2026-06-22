## Teoría y Metodología: Análisis de Registros de Interacción (CoreDuet)

Este documento detalla la estructura lógica de la base de datos `interactionC.db`, perteneciente al framework CoreDuet de Apple. Este artefacto es vital para reconstruir la actividad social del usuario, incluso cuando los historiales primarios han sido eliminados.

* **Ruta:** `/private/var/mobile/Library/CoreDuet/People/interactionC.db`

## 1. Análisis Estructural de Tablas (interactionC.db)

La base de datos contiene diversas tablas que gestionan tanto la heurística del dispositivo como los registros de usuario.

| Tabla | Descripción Técnica | Relevancia Forense |
| :--- | :--- | :--- |
| `ZINTERACTIONS` | Tabla principal: cada interacción registrada (llamada, mensaje, FaceTime). | Crítica |
| `ZCONTACTS` | Lista de contactos involucrados (números, emails, identificadores). | Crítica |
| `Z_1INTERACTIONS` | Tabla puente entre contactos y sus interacciones. | Importante |
| `Z_2INTERACTIONRECIPIENT` | Tabla puente entre interacciones y destinatarios. | Importante |
| `ZATTACHMENT` | Metadatos de adjuntos asociados a interacciones (frecuencia de uso muy baja). | Opcional |
| `ZKEYWORDS` / `Z_3KEYWORDS` | Palabras clave usadas por Siri/Spotlight y su tabla relacional. | Opcional |
| `ZVERSION` | Versión del modelo CoreDuet. | Sin relevancia |
| `Z_METADATA` | Metadatos internos del esquema de CoreData. | Sin relevancia |
| `Z_MODELCACHE` | Caché interna del modelo de aprendizaje heurístico. | Sin relevancia |
| `Z_PRIMARYKEY` | Control interno de claves primarias. | Sin relevancia |

## 2. Relaciones Lógicas para la Reconstrucción

Para mapear correctamente quién interactuó con quién y cuándo, se deben cruzar las tablas de la siguiente manera:

| Tabla Origen | Relación | Tabla Destino | Explicación |
| :--- | :--- | :--- | :--- |
| `ZINTERACTIONS` | 1:N | `Z_1INTERACTIONS` | Cada interacción puede estar asociada a uno o varios contactos. |
| `Z_1INTERACTIONS` | N:1 | `ZCONTACTS` | Identifica con qué contacto específico se produjo la interacción. |
| `ZINTERACTIONS` | 1:N | `Z_2INTERACTIONRECIPIENT` | Relaciona interacciones globales con destinatarios específicos. |
| `Z_2INTERACTIONRECIPIENT` | N:1 | `ZCONTACTS` | Identifica inequívocamente al destinatario de la interacción. |
| `ZINTERACTIONS` | 1:N | `Z_3KEYWORDS` | Asocia la interacción a los identificadores semánticos. |
| `Z_3KEYWORDS` | N:1 | `ZKEYWORDS` | Recupera el texto de las palabras clave de Siri/Spotlight. |



## 3. Evidencia Recuperable (Metadatos de Interacción)

La importancia de esta base de datos radica en que **preserva el rastro de las comunicaciones aunque el usuario haya borrado llamadas o mensajes de las aplicaciones nativas**. Se pueden extraer los siguientes datos reales (sin necesidad de inferencias):

* Fecha y hora exacta de la interacción.
* Tipo de interacción (`call`, `sms`, `imessage`, `facetime`).
* Identificador del contacto (Número de teléfono o Apple ID).
* Frecuencia de interacción con un contacto específico.
* Marca temporal (Timestamp) de la última vez que se interactuó.
* Aplicación utilizada (`com.apple.mobilephone`, `com.apple.MobileSMS`, `com.apple.facetime`).
* Duración de la comunicación (en el caso de llamadas de voz o vídeo).

## 4. Declaración para Informe Pericial

*Este bloque está redactado para ser incluido en la sección de metodología, alcance o hallazgos del dictamen:*

> "Se procedió al análisis técnico de la base de datos `interactionC.db`, ubicada en la ruta `/private/var/mobile/Library/CoreDuet/People/`. Esta base de datos pertenece al framework CoreDuet de iOS/iPadOS y actúa como un registro secundario (log) que almacena metadatos de las interacciones del usuario con sus contactos (tales como llamadas, mensajes de texto y comunicaciones vía FaceTime).
> 
> Aunque esta base de datos no almacena el contenido en texto plano de las comunicaciones o grabaciones de audio, sí conserva información estructurada sobre la existencia, frecuencia, fecha y tipo de interacción. Por tanto, su escrutinio permite certificar actividad de comunicaciones incluso en escenarios donde los historiales principales (como `CallHistory.storedata` o `sms.db`) han sido eliminados intencionalmente. Para este análisis, se han correlacionado las tablas `ZINTERACTIONS`, `ZCONTACTS`, `Z_1INTERACTIONS` y `Z_2INTERACTIONRECIPIENT`, logrando reconstruir la actividad relacional del dispositivo."

## 5. Consideraciones Analíticas Adicionales

Al examinar esta base de datos, el perito debe proceder a:
* Interpretar cada columna de `ZINTERACTIONS` para catalogar la tipología del contacto.
* Correlacionar los hallazgos de CoreDuet con las bases de datos de Mensajes y Llamadas para detectar discrepancias que evidencien un borrado intencional.
* Exportar las relaciones a una matriz temporal (tabla cronológica) para presentar la cadencia de la actividad en el informe final.
