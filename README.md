# Caso Práctico Forense: iPad

[![Forensic Tools](https://img.shields.io/badge/Forensic-iBackup%20Viewer%201.6.4-blue)](https://github.com/topics/ios-forensic)
[![SQLite](https://img.shields.io/badge/SQLite-DB%20Browser%203.13.1-green)](https://sqlitebrowser.org/)
[![Python](https://img.shields.io/badge/Python-3.x-yellow)](https://python.org)
[![ExifTool](https://img.shields.io/badge/EXIF-ExifToolGui%205.16-orange)](https://exiftool.org/)
[![iOS](https://img.shields.io/badge/iOS-14.4-lightgrey)](https://developer.apple.com/ios/)
[![License](https://img.shields.io/badge/License-MIT-red)](LICENSE)

> **Caso práctico forense:** Extracción y análisis de datos de un iPad (8ª generación) con iOS 14.4.  
> Realizado como parte de la formación en **Análisis Forense Informático** — Especialidad en dispositivos móviles iOS/iPadOS.

---

## Índice

- [Descripción General](#descripción-general)
- [Evidencias Adquiridas](#evidencias-adquiridas)
- [Hallazgos Clave](#hallazgos-clave)
- [Herramientas Utilizadas](#herramientas-utilizadas)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Metodología](#metodología)
- [Uso](#uso)
- [Licencia](#licencia)

---

## Descripción General

Este repositorio documenta la adquisición y el análisis forense completo de un **iPad (8ª generación)** con **iOS 14.4**. El examen se llevó a cabo utilizando herramientas forenses estándar del sector para extraer y analizar datos a partir de una copia de seguridad física (*backup*) del dispositivo.

### Objetivos

- Realizar la adquisición forense del iPad utilizando **iBackup Viewer 1.6.4.90**.
- Extraer y analizar cuentas, contactos, mensajes, registros de llamadas, archivos multimedia y notas.
- Examinar trazas de datos eliminados en las bases de datos del sistema (`SQLite`).
- Documentar los hallazgos siguiendo una metodología forense profesional.

---

## Evidencias Adquiridas

| Artefacto | Base de Datos / Origen | Estado |
|---|---|---|
| Cuenta de iCloud | `Accounts3.sqlite` — `ZACCOUNT` | ✅ Identificado |
| Propiedades de la cuenta | `ZACCOUNTPROPERTY` (NSKeyedArchiver) | ✅ Decodificado |
| Tipos de cuenta y credenciales | `ZACCOUNTTYPE` | ✅ Mapeado |
| SMS / iMessage | `sms.db` | ❌ Vacío (sin mensajes) |
| Historial de llamadas | `CallHistory.storedata` | ❌ Vacío (sin llamadas) |
| Fotos y vídeo | File system + `Photos.sqlite` | ✅ 3 archivos extraídos |
| Metadatos (EXIF) | `IMG_0004.HEIC`, `IMG_0004.MOV`, `IMG_0005.PNG` | ✅ Analizado |
| Notas | iBackup Viewer | ✅ 1 nota encontrada |
| Contactos | `AddressBook.sqlitedb` | ❌ Vacío |
| Multimedia eliminada | `Photos.sqlite` — `ZTRASHEDSTATE` | ✅ No se encontraron borrados |
| Credenciales del Keychain | `keychain-backup.plist` | 🔒 Cifrado (AES-GCM) |

---

## Hallazgos Clave

### Cuenta Principal

- **Email:** `vr.carlosiii@gmail.com`
- **Tipo:** iCloud (`com.apple.account.AppleAccount`)
- **Apple ID:** 21130402639
- **UUID:** `BE87C54F-B742-4394-9A56-E9E5933CE796`
- **Última configuración:** 2023-09-28 08:53:08 UTC

### Servicios de iCloud Activos

Fotos, Contactos, Calendarios, Recordatorios, Mail, Notas, Marcadores, Keychain, Buscar mi iPad, Salud, Mensajes en iCloud.

### Implicaciones

1. Los datos del usuario no se limitan a este dispositivo; existen copias en iCloud.
2. La sincronización del Keychain sugiere que las credenciales podrían recuperarse desde otros dispositivos Apple.
3. "Buscar mi iPad" genera registros de ubicación (*location logs*) relevantes para la línea de tiempo (*timeline*).
4. Con credenciales válidas, se pueden emitir solicitudes de preservación de datos a Apple.

### Evidencia Multimedia

| Archivo | Tipo | Fecha | Dispositivo | Notas |
|---|---|---|---|---|
| `IMG_0004.HEIC` | Live Photo | 2024-02-14 17:21 | iPad 8th Gen, iOS 14.4 | Contenido de clase, sin GPS |
| `IMG_0004.MOV` | Vídeo (2.5s) | 2024-02-14 16:21 UTC | Mismo dispositivo | HEVC 1440×1080, Content ID coincidente |
| `IMG_0005.PNG` | Captura de pantalla | 2024-12-04 15:00 | Mismo dispositivo | Diálogo de "Confiar en este ordenador" ("Trust This Computer?") |

---

## Herramientas Utilizadas

| Herramienta | Versión | Propósito |
|---|---|---|
| iBackup Viewer | 1.6.4.90 | Adquisición y exploración forense del *backup* |
| DB Browser for SQLite | 3.13.1 | Análisis de bases de datos (`Accounts3.sqlite`, `Photos.sqlite`, etc.) |
| ExifToolGui | 5.16.0.0 | Extracción de metadatos EXIF de archivos multimedia |
| Python 3 | — | Decodificadores personalizados (*custom decoders*) para datos NSKeyedArchiver |
| Dispositivos Apple | 1.6.4.90 | Generación de la imagen inicial del dispositivo |

---

## Estructura del Repositorio

```text
ipad-forensic-case-study/
├── README.md                           # Este archivo
├── reporte_analisis_forense_ipad.md    # Informe forense completo
├── hallazgos_clave.md                  # Resumen ejecutivo de los hallazgos
├── metodologia.md                      # Metodología forense aplicada
├── evidencias.md                       # Salidas de herramientas en formato ASCII visual
├── scripts/
│   ├── decodificar_nskeyed_es.py       # Decodificador de NSKeyedArchiver / Base64 / Plist
│   ├── buscar_cuentas.py               # Búsqueda de cuentas del Keychain desde XML
│   └── README.md                       # Documentación de los scripts
├── teoria/
│   └── (Documentos teóricos para contextos forenses)
└── evidencias/
    └── (Capturas de pantalla de las herramientas forenses)
