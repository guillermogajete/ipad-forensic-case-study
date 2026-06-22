# Metodología Forense Aplicada

> Proceso estructurado seguido para la adquisición y análisis del iPad 14 (iOS 14.4).

---

## Fase 1: Adquisición

**Objetivo:** Obtener una copia forense del dispositivo sin alterar la evidencia original.

| Paso | Acción | Herramienta |
|---|---|---|
| 1.1 | Conexión del dispositivo al equipo forense | Cable USB |
| 1.2 | Creación de backup cifrado | Dispositivo Apple 1.6.4.90 |
| 1.3 | Almacenamiento en ruta segura | `C:\Users\seguridad\Apple` |
| 1.4 | Copia a carpeta de trabajo | `Caso_Ipad` |
| 1.5 | Creación de estructura de exportación | `fichero_ipad_01052026/` |

**Recomendación:** Calcular hash (SHA-256) de la carpeta `Caso_Ipad` al inicio y al cierre del caso para garantizar la integridad.

---

## Fase 2: Análisis de Cuentas

**Objetivo:** Identificar todas las cuentas configuradas y sus propiedades.

| Paso | Base de Datos | Tablas | Propósito |
|---|---|---|---|
| 2.1 | `Accounts3.sqlite` | `ZACCOUNT` | Identificar cuentas principales |
| 2.2 | `Accounts3.sqlite` | `ZACCOUNTPROPERTY` | Propiedades extendidas (NSKeyedArchiver) |
| 2.3 | `Accounts3.sqlite` | `ZACCOUNTTYPE` | Tipos de cuenta y credenciales |
| 2.4 | `Accounts3.sqlite` | `ZCREDENTIALITEM` | Credenciales cifradas |
| 2.5 | Keychain | `keychain-backup.plist` | Contraseñas del llavero |

### Técnica: Decodificación NSKeyedArchiver

El campo `ZVALUE` de `ZACCOUNTPROPERTY` almacena datos en formato:
**Base64 → Plist binario → NSKeyedArchiver (UID resolution)**

Se desarrolló un script Python (`decodificar_nskeyed_es.py`) que realiza:
1. Decodificación Base64
2. Carga del Plist
3. Resolución de referencias UID
4. Conversión de Apple Absolute Time a fechas UTC/Local
5. Interpretación de booleanos, strings, arrays y diccionarios

---

## Fase 3: Comunicaciones

**Objetivo:** Recuperar mensajes y registros de llamadas.

| Artefacto | Ruta en backup | Tablas | Estado |
|---|---|---|---|
| SMS/iMessage | `System/mobile/Library/SMS/sms.db` | `message`, `chat`, `chat_message_join`, `chat_handle_join`, `sync_deleted_chats` | Vacío |
| Llamadas | `System/mobile/Library/CallHistoryDB/CallHistory.storedata` | `ZCALLRECORD` | Vacío |
| Transaction logs | `CallHistoryTransactions/transactions.log` | — | Vacío |

---

## Fase 4: Extracción Multimedia

**Objetivo:** Extraer y analizar archivos multimedia del dispositivo.

| Paso | Acción | Herramienta |
|---|---|---|
| 4.1 | Exportar archivos multimedia | iBackup Viewer |
| 4.2 | Analizar metadatos EXIF | ExifToolGui 5.16 |
| 4.3 | Verificar identificadores internos (Content ID, Photo ID) | ExifToolGui |
| 4.4 | Inspección visual del contenido | Visor de imágenes/video |

### Metadatos analizados por archivo

- **Información del archivo:** nombre, tamaño, tipo, fechas
- **Metadatos EXIF:** fabricante, modelo cámara, fecha, software, GPS
- **MakerNotes Apple:** Content Identifier, Photo Identifier, tipo de cámara, vector aceleración

---

## Fase 5: Análisis de Datos Eliminados

**Objetivo:** Determinar si existieron archivos o datos borrados.

| Base de Datos | Ruta | Tablas clave | Campos clave |
|---|---|---|---|
| `Photos.sqlite` | `mobile/Media/PhotoData` | `ZADDITIONALASSETATTRIBUTES` | `ZPTPTRASHEDSTATE` |
| `Photos.sqlite` | `mobile/Media/PhotoData` | `ZGENERICALBUM` | `ZTRASHEDSTATE`, `ZTRASHEDDATE` |
| `Photos.sqlite` | `mobile/Media/PhotoData` | `ZASSET` | `ZTRASHEDSTATE`, `ZTRASHEDDATE`, `ZVISIBILITYSTATE` |

### Estados de eliminación

| Valor | Significado |
|---|---|
| `0` | Normal / Visible |
| `1` | Eliminado recientemente / Papelera |
| `2` | Eliminado permanentemente |

---

## Fase 6: Contactos y Agenda

| Base de Datos | Ruta | Tablas |
|---|---|---|
| `AddressBook.sqlitedb` | `mobile/Library/AddressBook` | `ABPerson`, `ABPersonChanges`, `ABPersonMultiValueDeletes` |

---

## Fase 7: Registros del Sistema

| Base de Datos | Ruta | Propósito |
|---|---|---|
| `interactionC.db` | `mobile/Library/CoreDuet/People` | Registros de interacciones del usuario |

---

## Herramientas Utilizadas

| Herramienta | Versión | Uso en fases |
|---|---|---|
| Dispositivo Apple | 1.6.4.90 | Fase 1 |
| iBackup Viewer | 1.6.4.90 | Fases 1, 2, 3, 4 |
| DB Browser for SQLite | 3.13.1 | Fases 2, 3, 5, 6, 7 |
| ExifToolGui | 5.16.0.0 | Fase 4 |
| Python 3 + plistlib | — | Fase 2 (decodificación) |

---

## Referencias

- Apple Absolute Time: epoch `978307200` (1/1/2001)
- NSKeyedArchiver format: Apple's NSCoding archive format
- SQLite WAL mode: `-shm` and `-wal` files may contain uncommitted transactions
