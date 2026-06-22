# Reporte de Análisis Forense — iPad 14 (iOS 14.4)

**Examinador:** Guillermo Cañavate Gajete  
**Dispositivo:** iPad 14 (8th generation) — iOS 14.4  
**Fecha de adquisición:** 20/04/2026  
**Herramienta de adquisición:** Dispositivo Apple 1.6.4.90  
**Caso:** `Caso_Ipad`

---

## 1. Adquisición de la Evidencia

La copia de seguridad se realizó con la herramienta **Dispositivo Apple 1.6.4.90** y se almacenó en:

```
C:\Users\seguridad\Apple
```

El 20/04/2026 a las 19:43 se transfirió la evidencia a la carpeta de trabajo:

```
Ciberseguridad\Analisis Forense\Taller de Análisis Forense Informático\Móviles 5-7 (iOS y iPadOS)\Caso_Ipad
```

Se creó la carpeta `fichero_ipad_01052026` para exportar y analizar los datos del dispositivo.

### Estructura de la carpeta de evidencias

| Carpeta | Fecha | Contenido |
|---|---|---|
| `contactos_ipad14_03052026` | 03/05/2026 15:55 | Contactos |
| `cuentas_ipad14_02052026` | 03/05/2026 15:32 | Cuentas |
| `email_ipad14_03052026` | 03/05/2026 11:02 | Correo |
| `llamadas_ipad14_03052026` | 03/05/2026 11:02 | Registros de llamadas |
| `media_ipad14_01052026` | 03/05/2026 15:01 | Archivos multimedia |
| `notas_ipad14_01052026` | 02/05/2026 00:57 | Notas |
| `pass_cuentas_ipad14_02052026` | 02/05/2026 21:20 | Credenciales |
| `registro_ipad14_03052026` | 03/05/2026 15:02 | Registros del sistema |
| `SMS_03052026` | 03/05/2026 09:51 | Mensajes SMS/iMessage |

---

## 2. Análisis de Cuentas

### 2.1 Base de datos Accounts3.sqlite

**Ruta:** `System > mobile > Library > Accounts > VerifiedBackup`  
**Herramienta de extracción:** iBackup Viewer  
**Herramienta de análisis:** DB Browser for SQLite 3.13.1

#### 2.1.1 Tabla ZACCOUNT — Cuentas principales

La tabla `ZACCOUNT` contiene las cuentas configuradas en el dispositivo. Los hallazgos más relevantes:

| Campo | Valor |
|---|---|
| `ZUSERNAME` | `vr.carlosiii@gmail.com` |
| `ZACCOUNTDESCRIPTION` | iCloud |
| `ZOWNINGBUNDLEID` | `com.apple.account.AppleAccount` |
| `ZIDENTIFIER` (UUID) | `BE87C54F-B742-4394-9A56-E9E5933CE796` |
| `ZDATE` (timestamp) | `717583988.297471` |

**Resolución de timestamp:**  
`717583988.297471` (Apple Absolute Time) → **2023-09-28 08:53:08 UTC**

**Conclusión:**
- **Cuenta principal:** `vr.carlosiii@gmail.com`
- **Dispositivo:** iPad 14
- **Última configuración:** 28/09/2023 08:53:08 UTC

#### Servicios iCloud sincronizados

La cuenta tenía habilitada la sincronización con iCloud para los siguientes servicios:

| Servicio | Identificador |
|---|---|
| Fotos de iCloud | `com.apple.Dataclass.CloudPhotos` |
| Contactos | `com.apple.Dataclass.Contacts` |
| Calendarios | `com.apple.Dataclass.Calendars` |
| Recordatorios | `com.apple.Dataclass.Reminders` |
| Correo iCloud | `com.apple.Dataclass.Mail` |
| Notas | `com.apple.Dataclass.Notes` |
| Marcadores de Safari | `com.apple.Dataclass.Bookmarks` |
| Llavero de iCloud | `com.apple.Dataclass.KeychainSync` |
| Buscar mi iPad | `com.apple.Dataclass.DeviceLocator` |
| Buscar mis amigos | `com.apple.Dataclass.SearchParty` |
| Datos de Salud | `com.apple.Dataclass.Health` |
| Mensajes en la nube | `com.apple.Dataclass.Messagesi` |

#### 2.1.2 Tabla ZACCOUNTPROPERTY — Propiedades de cuenta

La tabla `ZACCOUNTPROPERTY` almacena información extendida de la cuenta. El campo `ZVALUE` contiene datos codificados en **NSKeyedArchiver + Base64 + Plist**.

Se utilizó el script [`decodificar_nskeyed_es.py`](scripts/decodificar_nskeyed_es.py) para decodificar dichos valores.

**Hallazgos decodificados:**

| Clave (`ZKEY`) | Valor |
|---|---|
| `primaryEmail` | `vr.carlosiii@gmail.com` |
| `firstName` | VR1 |
| `lastName` | Carlos III |
| `primaryAccount` | `true` |
| `regionInfo` | España |
| `personID` (Apple ID) | `21130402639` |
| `usesCloudDocs` | `true` (iCloud Drive activado) |

#### 2.1.3 Tabla ZACCOUNTTYPE — Tipos de cuenta

Relación de tipos de cuenta identificados en el dispositivo:

| Z_PK | Tipo de cuenta | Identificador | Tipo de credencial |
|---|---|---|---|
| 5 | iTunes Store | `com.apple.account.iTunesStore` | password |
| 31 | Holiday Calendar | `com.apple.account.HolidayCalendar` | password |
| 44 | IDMS | `com.apple.account.idms` | token |
| 10 | Apple ID Authentication | `com.apple.account.AppleIDAuthentication` | appleid-authentication |
| 50 | IdentityServices | `com.apple.account.IdentityServices` | token |
| 15 | Messages | `com.apple.account.CloudKit` | token |
| **13** | **iCloud** | **`com.apple.account.AppleAccount`** | **token** |
| 28 | IMAPNotes | `com.apple.account.IMAPNotes` | password |
| 8 | CardDAV | `com.apple.account.CardDAV` | password |
| 45 | CalDAV | `com.apple.account.CalDAV` | password |
| 9 | Device Locator | `com.apple.account.DeviceLocator` | token |
| 17 | Find My Friends | `com.apple.account.FindMyFriends` | token |
| 14 | iTunes Store (Sandbox) | `com.apple.account.iTunesStore.sandbox` | password |

La cuenta **Z_PK = 13** corresponde a la **cuenta iCloud principal**, configurada con autenticación mediante **token** (sin contraseña almacenada localmente).

#### 2.1.4 Tabla ZCREDENTIALITEM

Esta tabla contiene credenciales cifradas mediante **AES-GCM/CCM** y se encontró sin datos accesibles.

### 2.2 Keychain

Se localizó el fichero `keychain-backup.plist` mediante iBackup Viewer, que contiene las contraseñas cifradas. No fue posible el descifrado de las mismas.

---

## 3. Mensajes y Llamadas

### 3.1 Mensajes SMS/iMessage

**Base de datos:** `sms.db`  
**Ruta:** `System > mobile > Library > SMS`

Se revisaron las tablas `message`, `chat`, `chat_message_join`, `chat_handle_join` y `sync_deleted_chats`. **Todas se encontraron vacías**, lo que indica que no existían mensajes activos ni borrados en el dispositivo.

### 3.2 Registros de Llamadas

**Base de datos:** `CallHistory.storedata`  
**Ruta:** `System > mobile > Library > CallHistoryDB`

**Tabla analizada:** `ZCALLRECORD` — se encontró **vacía**, sin registros de llamadas entrantes, salientes o perdidas.

**Archivo de transacciones:** `transactions.log` en `CallHistoryTransactions` — también vacío.

No se encontró evidencia de que se hubieran borrado llamadas.

---

## 4. Extracción de Archivos Multimedia

El 01/05/2026 se realizó la extracción de archivos del dispositivo mediante **iBackup Viewer**, volcando los resultados a la carpeta `media_ipad14_01052026`.

### Archivos extraídos

| Archivo | Tamaño | Tipo |
|---|---|---|
| `IMG_0004.HEIC` | 1.668 KB | Live Photo |
| `IMG_0004.MOV` | 2.138 KB | Video HEVC |
| `IMG_0005.PNG` | 4.468 KB | Captura de pantalla |

### 4.1 Metadatos — IMG_0004.HEIC

**Herramienta:** ExifToolGui v5.16.0.0

| Parámetro | Valor |
|---|---|
| Fabricante | Apple |
| Modelo | iPad (8th generation) |
| Fecha original | 2024-02-14 17:21:03 |
| Software | iOS 14.4 |
| Content Identifier | `9EDD30F4-9E7B-4B3D-B9F0-16EA96BCC1F5` |
| Photo Identifier | `151090FD-69E8-44B3-AB56-FB38904F6902` |
| Tipo de cámara | Back Wide Angle |
| Vector de aceleración | `0.0049 -0.8415 -0.5269` |
| GPS | No presente |

**Análisis visual:** El video muestra un aula con ordenadores de sobremesa y mobiliario (mesa verde, silla). Se observa un portátil modelo AORUS ejecutando una máquina virtual de Windows 10 en VirtualBox.

### 4.2 Metadatos — IMG_0004.MOV

| Parámetro | Valor |
|---|---|
| Duración | 2.50 segundos |
| Resolución | 1440 × 1080 |
| Códec | HEVC (hvc1) |
| Fecha de captura | 2024-02-14 16:21:03 UTC |
| Dispositivo | Apple iPad (8th generation) |
| Rotación | 90° |
| Content Identifier | `9EDD30F4-9E7B-4B3D-B9F0-16EA96BCC1F5` |
| GPS | No presente |

El `Content Identifier` coincide con el de `IMG_0004.HEIC`, confirmando que ambos archivos pertenecen al mismo momento de captura (Live Photo).

### 4.3 Metadatos — IMG_0005.PNG

| Parámetro | Valor |
|---|---|
| Tipo | PNG — Captura de pantalla |
| Resolución | 1620 × 2160 |
| Fecha de captura | 2024-12-04 15:00:13 |
| Orientación | Horizontal |
| GPS | No presente |

**Contenido:** La captura muestra la pantalla del iPad con un diálogo del sistema:  
*"¿Confiar en este ordenador? Tus ajustes y datos estarán accesibles desde este ordenador si se conectan de forma inalámbrica o usando un cable."*

---

## 5. Notas

Se localizó una nota creada el **14/02/2024 a las 17:21:50** con el nombre **"PRUEBA JUAN JOSÉ ESPI"**. La nota no contenía contenido adicional relevante.

---

## 6. Archivos Borrados

### 6.1 Archivos multimedia

**Base de datos:** `Photos.sqlite`  
**Ruta:** `mobile > Media > PhotoData`

#### Tabla ZADDITIONALASSETATTRIBUTES

Campo `ZPTPTRASHEDSTATE`:
- `0` = Normal
- `1` = Eliminado recientemente
- `2` = Eliminado permanentemente

**Resultado:** Todos los registros muestran `ZPTPTRASHEDSTATE = 0`. No hay archivos eliminados.

#### Tabla ZGENERICALBUM

Campo `ZTRASHEDSTATE`:
- `0` = Álbum normal
- `1` = Álbum en papelera
- `2` = Álbum eliminado permanentemente

**Resultado:** Todos los registros con `ZTRASHEDSTATE = 0`. Sin álbumes eliminados. Campo `ZTRASHEDDATE` sin datos.

#### Tabla ZASSET

Campos analizados: `ZTRASHEDSTATE`, `ZTRASHEDDATE`, `ZVISIBILITYSTATE`.

**Resultado:** Todos los registros con `ZTRASHEDSTATE = 0`, `ZTRASHEDDATE` vacío, `ZVISIBILITYSTATE = 0` (visible). No existe ningún archivo multimedia eliminado u oculto.

### 6.2 Mensajes SMS

La base de datos `sms.db` se encontró completamente vacía, sin evidencia de mensajes borrados.

### 6.3 Registros de actividad

**Base de datos:** `interactionC.db`  
**Ruta:** `mobile > Library > CoreDuet > People`

No se encontró ningún registro de interacciones del usuario.

---

## 7. Contactos

**Base de datos:** `AddressBook.sqlitedb`  
**Ruta:** `mobile > Library > AddressBook`

Tablas analizadas:

| Tabla | Estado |
|---|---|
| `ABPerson` | Vacía — sin contactos |
| `ABPersonChanges` | Vacía — sin modificaciones |
| `ABPersonMultiValueDeletes` | Vacía — sin eliminaciones |

No existían contactos almacenados ni se había realizado ninguna operación de borrado sobre ellos.

---

## 8. Redes Sociales

Desde **iOS 11**, Apple no almacena en sus bases de datos locales los usuarios de redes sociales. Además, mediante iBackup Viewer se verificó que **no hay aplicaciones de redes sociales instaladas** en el dispositivo.

---

## 9. Implicaciones para la Investigación

1. Los datos del usuario **no están limitados a este dispositivo** — existen copias en iCloud.
2. Con credenciales válidas, se podría solicitar **preservación de datos a Apple**.
3. El **keychain sincronizado** sugiere que otras contraseñas podrían recuperarse desde otros dispositivos Apple del mismo usuario.
4. La activación de **"Buscar mi iPad"** genera logs de ubicación relevantes para la línea temporal.
5. El dispositivo se encontró con **mínima actividad de usuario**: sin mensajes, llamadas, contactos ni redes sociales.
6. La única evidencia de interacción activa son los **3 archivos multimedia** y **1 nota**.

---

## 10. Herramientas Utilizadas

| Herramienta | Versión | Propósito |
|---|---|---|
| Dispositivo Apple | 1.6.4.90 | Adquisición forense inicial |
| iBackup Viewer | 1.6.4.90 | Exploración y extracción del backup |
| DB Browser for SQLite | 3.13.1 | Análisis de bases de datos SQLite |
| ExifToolGui | 5.16.0.0 | Extracción de metadatos EXIF |
| Python 3 | — | Scripts personalizados de decodificación |

---

## 11. Ficheros del Caso

| Carpeta raíz | Contenido |
|---|---|
| `fichero_ipad_01052026/` | Datos exportados del iPad 14 |
| `Caso_Ipad/` | Carpeta principal del caso |

*Hash de la carpeta `fichero_ipad_01052026` y `Caso_Ipad` pendiente de cálculo al cierre del caso.*
