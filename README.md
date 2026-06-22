# iPad Forensic Case Study

[![Forensic Tools](https://img.shields.io/badge/Forensic-iBackup%20Viewer%201.6.4-blue)](https://github.com/topics/ios-forensic)
[![SQLite](https://img.shields.io/badge/SQLite-DB%20Browser%203.13.1-green)](https://sqlitebrowser.org/)
[![Python](https://img.shields.io/badge/Python-3.x-yellow)](https://python.org)
[![ExifTool](https://img.shields.io/badge/EXIF-ExifToolGui%205.16-orange)](https://exiftool.org/)
[![iOS](https://img.shields.io/badge/iOS-14.4-lightgrey)](https://developer.apple.com/ios/)
[![License](https://img.shields.io/badge/License-MIT-red)](LICENSE)

> **Case study forense:** Extracción y análisis de datos de un iPad 14 (8th generation) con iOS 14.4.  
> Realizado como parte de la formación en **Análisis Forense Informático** — Especialidad en dispositivos móviles iOS/iPadOS.

---

## Table of Contents

- [Overview](#overview)
- [Evidence Acquired](#evidence-acquired)
- [Key Findings](#key-findings)
- [Tools Used](#tools-used)
- [Repository Structure](#repository-structure)
- [Methodology](#methodology)
- [Usage](#usage)
- [License](#license)

---

## Overview

This repository documents a complete forensic acquisition and analysis of an **iPad 14 (8th generation)** running **iOS 14.4**. The examination was conducted using industry-standard forensic tools to extract and analyze data from a physical backup of the device.

### Objectives

- Perform a forensic acquisition of the iPad using **iBackup Viewer 1.6.4.90**
- Extract and analyze accounts, contacts, messages, call logs, media files, and notes
- Examine deleted data traces in system databases (`SQLite`)
- Document findings with professional forensic methodology

---

## Evidence Acquired

| Artifact | Database / Source | Status |
|---|---|---|
| iCloud account | `Accounts3.sqlite` — `ZACCOUNT` | ✅ Identified |
| Account properties | `ZACCOUNTPROPERTY` (NSKeyedArchiver) | ✅ Decoded |
| Account types & credentials | `ZACCOUNTTYPE` | ✅ Mapped |
| SMS / iMessage | `sms.db` | ❌ Empty (no messages) |
| Call history | `CallHistory.storedata` | ❌ Empty (no calls) |
| Photos & video | File system + `Photos.sqlite` | ✅ 3 files extracted |
| Metadata (EXIF) | `IMG_0004.HEIC`, `IMG_0004.MOV`, `IMG_0005.PNG` | ✅ Analyzed |
| Notes | iBackup Viewer | ✅ 1 note found |
| Contacts | `AddressBook.sqlitedb` | ❌ Empty |
| Deleted media | `Photos.sqlite` — `ZTRASHEDSTATE` | ✅ No deletions found |
| Keychain credentials | `keychain-backup.plist` | 🔒 Encrypted (AES-GCM) |

---

## Key Findings

### Primary Account

- **Email:** `vr.carlosiii@gmail.com`
- **Type:** iCloud (`com.apple.account.AppleAccount`)
- **Apple ID:** 21130402639
- **UUID:** `BE87C54F-B742-4394-9A56-E9E5933CE796`
- **Last configured:** 2023-09-28 08:53:08 UTC

### iCloud Services Active

Photos, Contacts, Calendars, Reminders, Mail, Notes, Bookmarks, Keychain, Find My iPad, Health, Messages in iCloud.

### Implications

1. User data is not limited to this device — iCloud copies exist
2. Keychain sync suggests credentials may be recoverable from other Apple devices
3. "Find My iPad" generates location logs relevant to the timeline
4. With valid credentials, data preservation requests can be filed with Apple

### Media Evidence

| File | Type | Date | Device | Notes |
|---|---|---|---|---|
| `IMG_0004.HEIC` | Live Photo | 2024-02-14 17:21 | iPad 8th Gen, iOS 14.4 | Classroom content, no GPS |
| `IMG_0004.MOV` | Video (2.5s) | 2024-02-14 16:21 UTC | Same device | HEVC 1440×1080, matched Content ID |
| `IMG_0005.PNG` | Screenshot | 2024-12-04 15:00 | Same device | "Trust This Computer?" dialog |

---

## Tools Used

| Tool | Version | Purpose |
|---|---|---|
| iBackup Viewer | 1.6.4.90 | Forensic backup acquisition & browsing |
| DB Browser for SQLite | 3.13.1 | Database analysis (`Accounts3.sqlite`, `Photos.sqlite`, etc.) |
| ExifToolGui | 5.16.0.0 | EXIF metadata extraction from media files |
| Python 3 | — | Custom decoders for NSKeyedArchiver data |
| Dispositivo Apple | 1.6.4.90 | Initial device imaging |

---

## Repository Structure

```
ipad-forensic-case-study/
├── README.md                           # This file
├── reporte_analisis_forense_ipad.md    # Full forensic report (Spanish)
├── hallazgos_clave.md                  # Executive summary of findings
├── metodologia.md                      # Forensic methodology applied
├── evidencias.md                       # Tool outputs in visual ASCII format
├── scripts/
│   ├── decodificar_nskeyed_es.py       # NSKeyedArchiver / Base64 / Plist decoder
│   ├── buscar_cuentas.py               # Keychain account search from XML
│   └── README.md                       # Scripts documentation
├── teoria/
│   └── (theory documents for forensic contexts)
└── evidencias/
    └── (screenshots from forensic tools)
```

---

## Methodology

The forensic process followed a structured approach:

1. **Acquisition** — Backup creation with iBackup Viewer 1.6.4.90
2. **Account Analysis** — `Accounts3.sqlite` review (ZACCOUNT, ZACCOUNTPROPERTY, ZACCOUNTTYPE)
3. **Communication Artifacts** — SMS (`sms.db`) and calls (`CallHistory.storedata`)
4. **Media Extraction** — Photos, videos, and metadata analysis via ExifTool
5. **Deleted Data** — `Photos.sqlite` trash state examination
6. **Notes & Contacts** — Verification of stored and deleted records
7. **Keychain** — Encrypted credential inspection

> See [`metodologia.md`](metodologia.md) for detailed step-by-step procedure.

---

## Usage

```bash
# Clone the repository
git clone https://github.com/yourusername/ipad-forensic-case-study.git

# Navigate to scripts
cd ipad-forensic-case-study/scripts

# Decode a Base64 ZVALUE from Accounts3.sqlite
python decodificar_nskeyed_es.py "YnBsaXN0MDDUAQIDBAU..."

# Search for accounts in a keychain XML export
python buscar_cuentas.py
```

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <b>Mobile Forensic Analysis · iOS · iPadOS · iCloud Forensics</b>
</p>
