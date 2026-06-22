# Hallazgos Clave — Análisis Forense iPad 14

> Resumen ejecutivo de los hallazgos más relevantes del caso.

---

## 1. Identidad del Dispositivo y Usuario

| Dato | Valor |
|---|---|
| Dispositivo | iPad 14 (8th generation), iOS 14.4 |
| Correo principal | `vr.carlosiii@gmail.com` |
| Nombre asociado | VR1 Carlos III |
| Apple ID | `21130402639` |
| UUID de cuenta | `BE87C54F-B742-4394-9A56-E9E5933CE796` |
| Última configuración | 28/09/2023 08:53:08 UTC |

## 2. Servicios iCloud Activos

Fotos, Contactos, Calendarios, Recordatorios, Mail, Notas, Marcadores, **Llavero iCloud**, Buscar mi iPad, Salud, Mensajes en iCloud.

> El llavero sincronizado implica que contraseñas de otros dispositivos Apple del usuario podrían ser accesibles.

## 3. Estado del Dispositivo

El dispositivo presentaba una **actividad mínima de usuario**:

| Artefacto | Estado |
|---|---|
| SMS / iMessage | Sin datos |
| Llamadas | Sin registros |
| Contactos | Sin datos |
| Redes sociales | Sin aplicaciones instaladas |
| Notas | 1 nota: "PRUEBA JUAN JOSÉ ESPI" (14/02/2024) |
| Archivos multimedia | 3 archivos (2 de un mismo Live Photo, 1 captura) |
| Archivos eliminados | No se detectaron eliminaciones |

## 4. Evidencia Multimedia

| Archivo | Tipo | Fecha de captura | Detalle |
|---|---|---|---|
| `IMG_0004.HEIC` | Live Photo | 14/02/2024 17:21 | Aula con ordenadores, portátil AORUS, VM Windows 10 |
| `IMG_0004.MOV` | Video (2.5s) | 14/02/2024 16:21 UTC | Mismo contenido que HEIC, HEVC 1440×1080 |
| `IMG_0005.PNG` | Captura de pantalla | 04/12/2024 15:00 | Diálogo "¿Confiar en este ordenador?" |

Ninguno contenía datos GPS.

## 5. Credenciales

- Las contraseñas almacenadas en `keychain-backup.plist` están **cifradas con AES-GCM/CCM**
- No fue posible su descifrado en esta fase
- La cuenta iCloud usa **autenticación por token** (no almacena contraseña localmente)

## 6. Implicaciones Forenses

1. Los datos no están solo en el dispositivo — existen **copias en iCloud**
2. Con credenciales válidas se puede solicitar **preservación de datos a Apple**
3. El keychain sincronizado permite recuperación de contraseñas desde **otros dispositivos Apple**
4. "Buscar mi iPad" puede aportar **logs de ubicación** para la línea temporal

---

## Habilidades Demostradas

- Adquisición forense de dispositivos iOS/iPadOS
- Análisis de bases de datos SQLite (`Accounts3`, `Photos`, `sms`, `CallHistory`, etc.)
- Decodificación de formatos propietarios Apple (NSKeyedArchiver, Plist, Apple Absolute Time)
- Extracción y análisis de metadatos EXIF
- Documentación forense conforme a buenas prácticas
- Python para herramientas forenses personalizadas
