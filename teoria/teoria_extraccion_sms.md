## Teoría y Metodología: Extracción de Mensajería (SMS/iMessage)

Este documento detalla la estructura lógica de la base de datos `sms.db` en entornos iPadOS/iOS, esencial para la reconstrucción de conversaciones y la identificación de evidencia forense, incluyendo datos eliminados.

* **Ruta:** `/private/var/mobile/Library/SMS/sms.db`

## 1. Análisis de Tablas en sms.db

La base de datos se compone de múltiples tablas, clasificadas según su relevancia para la investigación forense.

| Tabla | Descripción | Relevancia Forense |
| :--- | :--- | :--- |
| `message` | Contenido del mensaje, timestamps, estado y tipo. | Crítica |
| `handle` | Identificadores de participantes (Teléfono/Apple ID). | Crítica |
| `chat` | Conversaciones individuales o grupos. | Crítica |
| `attachment` | Multimedia: fotos, vídeos, notas de audio, documentos. | Crítica |
| `deleted_messages` | Metadatos de mensajes eliminados. | Oro forense |
| `chat_message_join` | Relaciona mensajes con chats. | Importante |
| `chat_handle_join` | Relaciona chats con participantes. | Importante |
| `message_attachment_join` | Relaciona mensajes con adjuntos. | Importante |
| `sync_deleted_*` | Rastros de elementos eliminados vía iCloud. | Útil |

*Nota: Tablas como `_SqliteDatabaseProperties`, `kvtable`, `sqlite_sequence` y `sqlite_stat1` son de control interno y carecen de valor probatorio.*

## 2. Relaciones Lógicas entre Tablas

Para reconstruir una conversación, es necesario realizar *joins* entre las tablas siguiendo este esquema relacional:

| Tabla Origen | Relación | Tabla Destino | Explicación |
| :--- | :--- | :--- | :--- |
| `message` | 1:N | `chat_message_join` | Asociación de mensaje a su chat. |
| `chat_message_join` | N:1 | `chat` | Identificación del contenedor de chat. |
| `chat` | 1:N | `chat_handle_join` | Identificación de participantes en grupos. |
| `chat_handle_join` | N:1 | `handle` | Detalle del contacto (número/Apple ID). |
| `message` | 1:N | `message_attachment_join` | Vinculación de adjuntos al mensaje. |
| `message_attachment_join` | N:1 | `attachment` | Acceso a metadatos del archivo adjunto. |
| `message` | 1:1 | `deleted_messages` | Rastro de mensaje eliminado. |
| `message` | 1:1 | `sync_deleted_messages` | Rastro de mensaje eliminado vía iCloud. |
| `attachment` | 1:1 | `sync_deleted_attachments` | Adjuntos eliminados sincronizados. |
| `chat` | 1:1 | `sync_deleted_chats` | Chats eliminados sincronizados. |

## 3. Metodología de Reconstrucción de Evidencia Eliminada

El análisis de registros eliminados es fundamental para la integridad del informe. Se deben consultar las siguientes tablas para verificar indicios de actividad borrada:

* **`deleted_messages`**: Contiene metadatos de mensajes cuya entrada principal en `message` ha sido marcada como eliminada o purgada.
* **`sync_deleted_messages` / `sync_deleted_chats` / `sync_deleted_attachments`**: Estas tablas son determinantes si el dispositivo presenta sincronización activa con iCloud, ya que registran el *id* de los elementos eliminados a través de la cuenta vinculada, proporcionando trazabilidad incluso cuando el contenido original ya no es accesible.

## 4. Consideraciones Técnicas Forenses

* **Atribución**: La tabla `handle` es la única fuente fiable para la atribución de autoría. Se debe cruzar con la base de datos de contactos para identificar nombres reales.
* **Integridad Multimedia**: Siempre verificar la integridad de los archivos vinculados en la tabla `attachment`. La existencia de un registro en `attachment` sin su archivo físico correspondiente puede indicar una eliminación selectiva o una falla en la sincronización.
* **Contexto de Eliminación**: La presencia de registros en las tablas `sync_deleted_*` no garantiza la recuperación del contenido, pero constituye una prueba fehaciente de la existencia previa del dato y su posterior supresión mediante el ecosistema Apple.
