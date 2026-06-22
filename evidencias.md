# Evidencias Forenses — Salidas de Herramientas

> Representación textual de las capturas de las herramientas forenses utilizadas durante el análisis.

---

## 1. iBackup Viewer — Extracción de Accounts3.sqlite

```yaml
Tool: iBackup Viewer 1.6.4.90
Device: iPad 14 (8th generation)
iOS_Version: 14.4
Backup_Location: C:\Users\seguridad\Apple
Serial: [REDACTED]
Status: [✓] Accounts3.sqlite exported successfully
Extraction_Path: System > mobile > Library > Accounts > VerifiedBackup
```

---

## 2. DB Browser for SQLite — Tabla ZACCOUNT

**Base de Datos:** `Accounts3.sqlite` | **Tabla:** `ZACCOUNT`

| Z_PK | ZUSERNAME | ZACCOUNTDESCRIPTION | ZIDENTIFIER | ZOWNINGBUNDLEID | ZDATE |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **7** | `vr.carlosiii@gmail…` | iCloud | `BE87C54F-B742...` | `com.apple.account.AppleAccount` | `717583988.297471` |

**Decodificación del Timestamp (Apple Absolute Time):**

```text
Valor original: 717583988.297471
Epoch Base:     978307200 (01/01/2001 00:00:00 UTC)
Unix TS:        1695891188.297471
UTC:            2023-09-28 08:53:08
Local:          2023-09-28 10:53:08 (UTC+2)

Dale un vistazo en tu vista previa. Si todo cuadra y se ve profesional, ¡mándame la **Sección 3**!
```
```text
### Timestamp Decoded

Apple Absolute Time: 717583988.297471
          Epoch:     978307200 (01/01/2001 00:00:00 UTC)
          ─────────────────────────────────────────
          Unix TS:   1695891188.297471
          ─────────────────────────────────────────
          UTC:       2023-09-28 08:53:08
          Local:     2023-09-28 10:53:08 (UTC+2)
```
---

## 3. DB Browser for SQLite — Tabla ZACCOUNTTYPE

**Base de Datos:** `Accounts3.sqlite` | **Tabla:** `ZACCOUNTTYPE`

| PK | Type | Identifier |
| :--- | :--- | :--- |
| 5 | iTunes Store | `com.apple.account.iTunesStore` |
| 31 | Holiday Calendar | `com.apple.account.HolidayCalendar` |
| 44 | IDMS | `com.apple.account.idms` |
| 10 | Apple ID Authentication | `com.apple.account.AppleIDAuthentication` |
| 50 | IdentityServices | `com.apple.account.IdentityServices` |
| 15 | Messages | `com.apple.account.CloudKit` |
| **13** | **iCloud (MAIN)** | `com.apple.account.AppleAccount` |
| 28 | IMAPNotes | `com.apple.account.IMAPNotes` |
| 8 | CardDAV | `com.apple.account.CardDAV` |
| 45 | CalDAV | `com.apple.account.CalDAV` |
| 9 | Device Locator | `com.apple.account.DeviceLocator` |
| 17 | Find My Friends | `com.apple.account.FindMyFriends` |
| 14 | iTunes Store (Sandbox) | `com.apple.account.iTunesStore` |


---

## 4. Decodificador NSKeyedArchiver — ZVALUE

**Ejecución del script `decodificar_nskeyed_es.py`:**

```yaml
[1/4] Base64 Decode: [OK] 276 bytes decoded
[2/4] Plist Parse: [OK] NSKeyedArchiver format detected
[3/4] UID Resolution: [OK] All references resolved
[4/4] Value Interpretation: [OK]

# Resultados Decodificados:
primaryEmail:   xxxxxxxi@gmail.com
firstName:      VR1
lastName:       Carlos III
primaryAccount: true
regionInfo:     España
personID:       2113xxxxxxx
usesCloudDocs:  true
```
---
## 5. DB Browser for SQLite — Tabla ZACCOUNTPROPERTY

**Base de Datos:** `Accounts3.sqlite` | **Tabla:** `ZACCOUNTPROPERTY`

| Z_PK | ZKEY | ZVALUE (Decodificado) |
| :--- | :--- | :--- |
| 6 | primaryEmail | `xxxxxxxx@gmail.com` |
| 7 | firstName | `VR1` |
| 8 | lastName | `xxxxxxxxx` |
| 9 | primaryAccount | `true` |
| 10 | regionInfo | `España` |
| 11 | personID | `2113xxxxxxxxxx` |
| 12 | usesCloudDocs | `true` |

> *Nota: Todos los valores han sido procesados y decodificados utilizando el script `decodificar_nskeyed_es.py`.*

---
## 6. ExifToolGui — Metadatos IMG_0004.HEIC

### Información del Archivo
| Propiedad | Valor |
| :--- | :--- |
| **Nombre** | `IMG_0004.HEIC` |
| **Tamaño** | 1668 kB |
| **Tipo** | HEIC |
| **Creado** | 2026-05-01 20:16:09 |
| **Modificado** | 2026-05-01 20:16:10 |

### Metadatos EXIF
| Propiedad | Valor |
| :--- | :--- |
| **Fabricante** | Apple |
| **Modelo** | iPad (8th generation) |
| **Fecha Original** | 2024-02-14 17:21:03 |
| **Software** | iOS 14.4 |
| **GPS** | [No presente] |

### MakerNotes (Apple)
| Propiedad | Valor |
| :--- | :--- |
| **Content Identifier** | `9EDD30F4-9E7B-4B3D-B9F0-16EA96B...` |
| **Photo Identifier** | `151090FD-69E8-44B3-AB56-FB38904...` |
| **Tipo de Cámara** | Back Wide Angle |
| **Vector Aceleración** | 0.0049 -0.8415 -0.5269 |

---
## 7. ExifToolGui — Metadatos IMG_0004.MOV

### Información técnica y de captura
| Propiedad | Valor |
| :--- | :--- |
| **Nombre** | `IMG_0004.MOV` |
| **Duración** | 2.50 segundos |
| **Resolución** | 1440 × 1080 |
| **Códec** | HEVC (hvc1) |
| **Fecha Captura** | 2024-02-14 16:21:03 UTC |
| **Dispositivo** | Apple iPad (8th generation) |
| **Rotación** | 90° |
| **GPS** | [No presente] |

### Relación de Evidencia
| Propiedad | Valor |
| :--- | :--- |
| **Content ID** | `9EDD30F4-9E7B-4B3D-B9F0-16EA96BCC1F5` |
| **Notas Forenses** | ⚠ Coincide con `IMG_0004.HEIC` (mismo evento de *Live Photo*) |

---
## 8. ExifToolGui — Metadatos IMG_0005.PNG

### Información técnica
| Propiedad | Valor |
| :--- | :--- |
| **Nombre** | `IMG_0005.PNG` |
| **Tipo** | PNG — Screenshot |
| **Resolución** | 1620 × 2160 |
| **Tamaño** | 4.5 MB |
| **Fecha Captura** | 2024-12-04 15:00:13 |
| **Orientación** | Horizontal |
| **GPS** | [No presente] |

### Contenido Visual (OCR)
> **¿Confiar en este ordenador?**
> Tus ajustes y datos estarán accesibles desde este ordenador si se conectan de forma inalámbrica o usando un cable.
> 
> `[ Confiar ]`  `[ No confiar ]`
---
## 9. DB Browser for SQLite — Photos.sqlite (Deleted Media Check)

**Base de Datos:** `Photos.sqlite`

### Estado de los Activos Multimedia

| Tabla | Columna Analizada | Estado Detectado | Significado |
| :--- | :--- | :--- | :--- |
| `ZADDITIONALASSETATTRIBUTES` | `ZPTPTRASHEDSTATE` | 0 | Normal (No eliminado) |
| `ZASSET` | `ZTRASHEDSTATE` | 0 | Normal (No eliminado) |
| `ZASSET` | `ZVISIBILITYSTATE` | 0 | Visible |

### Análisis de Álbumes
* **Tabla `ZGENERICALBUM`:** * `ZTRASHEDSTATE` = 0 (Normal).
    * `ZTRASHEDDATE` = `NULL` (No hay fechas de borrado registradas).
    * ⚠ **Hallazgo:** No se detectó el álbum de "Eliminado Recientemente" (*Recently Deleted*).

> **Conclusión Forense:** Tras el análisis exhaustivo de las tablas relacionadas con la gestión de activos y álbumes, **no se han detectado archivos multimedia eliminados, ocultos o movidos a la papelera** en el momento de la extracción.
Entry 5: ... (15 entries total)
---
---

## 11. DB Browser for SQLite — sms.db (Comunicaciones)

**Base de Datos:** `sms.db`

| Tabla | Registros | Estado |
| :--- | :--- | :--- |
| `message` | 0 | 📭 Vacío |
| `chat` | 0 | 📭 Vacío |
| `chat_message_join` | 0 | 📭 Vacío |
| `chat_handle_join` | 0 | 📭 Vacío |
| `sync_deleted_chats` | 0 | 📭 Vacío |

> **Conclusión Forense:** Tras la inspección de todas las tablas críticas relacionadas con la mensajería, **se confirma que el dispositivo no contiene mensajes (ni activos ni eliminados/rastros de sincronización)**.

---
## 12. DB Browser for SQLite — CallHistory.storedata

**Base de Datos:** `CallHistory.storedata`

* **Tabla `ZCALLRECORD`:** 0 registros retornados.
* **Estado del log:** ⚠ El archivo `transactions.log` asociado también se encuentra vacío.

> **Conclusión Forense:** No se ha recuperado historial de llamadas en el dispositivo analizado.

---

## 13. iBackup Viewer — Contactos

**Base de Datos:** `AddressBook.sqlitedb`

| Tabla | Registros | Estado |
| :--- | :--- | :--- |
| `ABPerson` | 0 | 📇 Vacío |
| `ABPersonChanges` | 0 | 📭 Sin modificaciones |
| `ABPersonMultiValue` | 0 | 📭 Sin eliminaciones |

> **Resultado:** No se han encontrado contactos almacenados en el dispositivo analizado.

---
## 14. iBackup Viewer — Notas

**Herramienta:** `iBackup Viewer 1.6.4.90` | **Exportación:** `Notes`

| Atributo | Detalle |
| :--- | :--- |
| **Título** | `PRUEBA JUAN JOSÉ ESPI` |
| **Fecha Creación** | `2024-02-14 17:21:50` |
| **Contenido** | `[Vacío]` |

> **Observación:** Se ha detectado una única nota en el sistema, la cual no contiene texto ni archivos adjuntos.

---
## 15. DB Browser for SQLite — interactionC.db

**Base de Datos:** `interactionC.db`
**Ruta:** `mobile/Library/CoreDuet/People`

* **Tabla analizada:** `ZINTERACTIONS`
* **Registros encontrados:** 0

> **Conclusión Forense:** No se han recuperado registros de interacción de usuario en la base de datos de CoreDuet.

---
## 16. iBackup Viewer — Aplicaciones Instaladas

**Herramienta:** `iBackup Viewer 1.6.4.90`

### Aplicaciones de Sistema
* Settings, Safari, Photos, Camera, Notes, Contacts, Phone, Messages, FaceTime, App Store

### Aplicaciones de Terceros
| Estado | Detalle |
| :--- | :--- |
| ⚠️ **Sin resultados** | No se encontraron aplicaciones de terceros instaladas. |
| ⚠️ **Sin resultados** | No se detectaron aplicaciones de redes sociales en el dispositivo. |

> **Observación:** El análisis de aplicaciones instaladas indica que el dispositivo se encuentra en una configuración básica, operando únicamente con el conjunto de aplicaciones nativas de Apple.

---
