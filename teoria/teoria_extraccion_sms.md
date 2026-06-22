# Teoria Extraccion Sms

Tablas sms.db

Tabla

Descripción breve

_SqliteDatabaseProperties

Metadatos internos de SQLite (versión, flags). No contiene datos útiles de mensajes.

attachment

Registra archivos adjuntos enviados/recibidos: fotos, vídeos, notas de audio, documentos. Incluye ruta, tipo MIME, tamaño.

chat

Representa cada conversación (individual o grupo). Contiene identificadores, nombre del grupo, flags, estado.

chat_handle_join

Tabla puente que relaciona chats con participantes (handles).

chat_message_join

Tabla puente que relaciona chats con mensajes.

deleted_messages

Registra mensajes eliminados (solo metadatos básicos). Muy útil en informes.

handle

Lista de participantes: números de teléfono, Apple IDs, emails. Identifica a cada interlocutor.

kvtable

Tabla de pares clave‑valor usada por iMessage para configuraciones internas. No suele aportar evidencia.

message

La tabla principal: contiene cada mensaje enviado/recibido, timestamps, flags, estado, texto, tipo.

message_attachment_join

Relación entre mensajes y adjuntos. Un mensaje puede tener varios adjuntos.

message_processing_task

Tareas internas de procesamiento de mensajes. No suele aportar evidencia.

sqlite_sequence

Control interno de autoincremento. No contiene evidencia.

sqlite_stat1

Estadísticas de índices para el optimizador de SQLite. No contiene evidencia.

sync_deleted_attachments

Registra adjuntos eliminados sincronizados vía iCloud.

sync_deleted_chats

Registra chats eliminados sincronizados vía iCloud.

sync_deleted_messages

Registra mensajes eliminados sincronizados vía iCloud.

TABLAS RECOMENDADAS PARA UN INFORME FORENSE

Tabla

Por qué es importante

message

Contiene el contenido del mensaje, timestamps, estado, tipo. Es la tabla central.

handle

Identifica a cada interlocutor (número, Apple ID). Necesaria para atribución.

chat

Permite saber si el mensaje pertenece a un chat individual o grupo.

chat_message_join

Relaciona cada mensaje con su chat. Necesaria para reconstruir conversaciones.

chat_handle_join

Permite saber quién participa en cada chat (grupos).

attachment

Evidencia multimedia: fotos, vídeos, notas de voz.

message_attachment_join

Relaciona mensajes con adjuntos.

deleted_messages

Oro puro en informes: evidencia de mensajes eliminados.

sync_deleted_messages

Indica mensajes eliminados sincronizados con iCloud.

Opcionales pero útiles:

Tabla

Utilidad

sync_deleted_chats

Chats eliminados sincronizados.

sync_deleted_attachments

Adjuntos eliminados sincronizados.

No relevantes:

sqlite_stat1

sqlite_sequence

kvtable

message_processing_task

_SqliteDatabaseProperties

TABLA — Relaciones entre tablas y cómo se conectan

Tabla origen

Relación

Tabla destino

Explicación

message

1:N

chat_message_join

Cada mensaje puede pertenecer a uno o varios chats (normalmente uno).

chat_message_join

N:1

chat

Permite saber a qué chat pertenece cada mensaje.

chat

1:N

chat_handle_join

Un chat puede tener varios participantes (grupos).

chat_handle_join

N:1

handle

Cada participante se identifica por su handle (número/Apple ID).

message

1:N

message_attachment_join

Un mensaje puede tener varios adjuntos.

message_attachment_join

N:1

attachment

Relaciona cada adjunto con su mensaje.

message

1:1

deleted_messages

Si un mensaje fue eliminado, aparece aquí.

message

1:1

sync_deleted_messages

Si fue eliminado y sincronizado vía iCloud.

attachment

1:1

sync_deleted_attachments

Adjuntos eliminados sincronizados.

chat

1:1

sync_deleted_chats

Chats eliminados sincronizados.