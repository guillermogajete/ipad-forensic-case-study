# Evidencias Forenses — Salidas de Herramientas

> Representación textual de las capturas de las herramientas forenses utilizadas durante el análisis.

---

## 1. iBackup Viewer — Extracción de Accounts3.sqlite

```
╔══════════════════════════════════════════════════════════════════╗
║                    iBackup Viewer 1.6.4.90                      ║
║                    iPad 14 (8th generation)                     ║
╠══════════════════════════════════════════════════════════════════╣
║  Backup Location: C:\Users\seguridad\Apple                      ║
║  Device Name: iPad 14                                           ║
║  iOS Version: 14.4                                              ║
║  Serial: [REDACTED]                                             ║
║                                                                  ║
║  [✓] Accounts3.sqlite exported successfully                     ║
║  [✓] Path: System > mobile > Library > Accounts > VerifiedBackup║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 2. DB Browser for SQLite — Tabla ZACCOUNT

```
┌─────────────────────────────────────────────────────────────────┐
│              DB Browser for SQLite 3.13.1                       │
│              File: Accounts3.sqlite                             │
├─────────────────────────────────────────────────────────────────┤
│ Table: ZACCOUNT                                                 │
│                                                                  │
│ ┌──────┬──────────────────────┬──────────────────────────────┐  │
│ │ Z_PK │ ZUSERNAME            │ ZACCOUNTDESCRIPTION          │  │
│ ├──────┼──────────────────────┼──────────────────────────────┤  │
│ │  7   │ vr.carlosiii@gmail…  │ iCloud                       │  │
│ │  …   │ …                    │ …                            │  │
│ └──────┴──────────────────────┴──────────────────────────────┘  │
│                                                                  │
│ ┌──────┬────────────────────────────────────────────────────┐   │
│ │ Z_PK │ ZIDENTIFIER                                        │   │
│ ├──────┼────────────────────────────────────────────────────┤   │
│ │  7   │ BE87C54F-B742-4394-9A56-E9E5933CE796              │   │
│ └──────┴────────────────────────────────────────────────────┘   │
│                                                                  │
│ ┌──────┬──────────────────────────────┬──────────────────────┐  │
│ │ Z_PK │ ZOWNINGBUNDLEID              │ ZDATE                │  │
│ ├──────┼──────────────────────────────┼──────────────────────┤  │
│ │  7   │ com.apple.account.AppleAcc…  │ 717583988.297471     │  │
│ └──────┴──────────────────────────────┴──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Timestamp Decoded

```
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

```
┌─────────────────────────────────────────────────────────────────┐
│              DB Browser for SQLite 3.13.1                       │
│              Table: ZACCOUNTTYPE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PK  │ Type                    │ Identifier                      │
│ ─────┼─────────────────────────┼──────────────────────────────── │
│   5  │ iTunes Store            │ com.apple.account.iTunesStore   │
│  31  │ Holiday Calendar        │ com.apple.account.HolidayCal…  │
│  44  │ IDMS                    │ com.apple.account.idms         │
│  10  │ Apple ID Authentication │ com.apple.account.AppleIDAu…   │
│  50  │ IdentityServices        │ com.apple.account.IdentitySe…  │
│  15  │ Messages                │ com.apple.account.CloudKit     │
│ ═══13 ══ iCloud ════════════════║ com.apple.account.AppleAcc… ═══│  ← MAIN
│  28  │ IMAPNotes               │ com.apple.account.IMAPNotes    │
│   8  │ CardDAV                 │ com.apple.account.CardDAV      │
│  45  │ CalDAV                  │ com.apple.account.CalDAV       │
│   9  │ Device Locator          │ com.apple.account.DeviceLoc…   │
│  17  │ Find My Friends         │ com.apple.account.FindMyFriends│
│  14  │ iTunes Store (Sandbox)  │ com.apple.account.iTunesSto…   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Decodificador NSKeyedArchiver — ZVALUE

```
╔══════════════════════════════════════════════════════════════════╗
║         DECODIFICADOR FORENSE UNIVERSAL ZVALUE v1.0             ║
╚══════════════════════════════════════════════════════════════════╝

[1/4] Base64 Decode
      Input: YnBsaXN0MDDUAQIDBAUGBwpYJHZlcnNpb25ZJGFyY2hpdmVy...
      ──────> [OK] 276 bytes decoded

[2/4] Plist Parse
      ──────> [OK] NSKeyedArchiver format detected

[3/4] UID Resolution
      ──────> [OK] All references resolved

[4/4] Value Interpretation
      ──────> [OK]

┌────────────────────────────────────────────────────────────────┐
│  RESULTADOS DECODIFICADOS                                      │
├────────────────────────────────────────────────────────────────┤
│  primaryEmail    │  vr.carlosiii@gmail.com                     │
│  firstName       │  VR1                                        │
│  lastName        │  Carlos III                                 │
│  primaryAccount  │  true                                       │
│  regionInfo      │  España                                     │
│  personID        │  21130402639                                │
│  usesCloudDocs   │  true                                       │
└────────────────────────────────────────────────────────────────┘
```

---

## 5. DB Browser for SQLite — Tabla ZACCOUNTPROPERTY

```
┌─────────────────────────────────────────────────────────────────┐
│              DB Browser for SQLite 3.13.1                       │
│              Table: ZACCOUNTPROPERTY                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Z_PK │ ZKEY              │ ZVALUE (Base64 → NSKeyedArchiver)   │
│ ──────┼───────────────────┼────────────────────────────────────  │
│   6   │ primaryEmail      │ YnBsaXN0MDDUAQIDBAU...  → decoded   │
│   7   │ firstName         │ YnBsaXN0MDDUAQIDBAU...  → decoded   │
│   8   │ lastName          │ YnBsaXN0MDDUAQIDBAU...  → decoded   │
│   9   │ primaryAccount    │ YnBsaXN0MDDUAQIDBAU...  → decoded   │
│  10   │ regionInfo        │ YnBsaXN0MDDUAQIDBAU...  → decoded   │
│  11   │ personID          │ YnBsaXN0MDDUAQIDBAU...  → decoded   │
│  12   │ usesCloudDocs     │ YnBsaXN0MDDUAQIDBAU...  → decoded   │
│                                                                  │
│  → All values decoded with decodificar_nskeyed_es.py            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. ExifToolGui — Metadatos IMG_0004.HEIC

```
┌─────────────────────────────────────────────────────────────────┐
│              ExifToolGui 5.16.0.0                               │
│              File: IMG_0004.HEIC                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌── File Information ──────────────────────────────────────┐   │
│  │ File Name        │  IMG_0004.HEIC                        │   │
│  │ File Size        │  1668 kB                              │   │
│  │ File Type        │  HEIC                                 │   │
│  │ Created          │  2026-05-01 20:16:09                  │   │
│  │ Modified         │  2026-05-01 20:16:10                  │   │
│  └──────────────────┴───────────────────────────────────────┘   │
│                                                                  │
│  ┌── EXIF Metadata ─────────────────────────────────────────┐   │
│  │ Make             │  Apple                                 │   │
│  │ Camera Model     │  iPad (8th generation)                 │   │
│  │ Original Date    │  2024-02-14 17:21:03                   │   │
│  │ Software         │  iOS 14.4                              │   │
│  │ GPS              │  [Not present]                         │   │
│  └──────────────────┴───────────────────────────────────────┘   │
│                                                                  │
│  ┌── MakerNotes (Apple) ────────────────────────────────────┐   │
│  │ Content Identifier │  9EDD30F4-9E7B-4B3D-B9F0-16EA96B…  │   │
│  │ Photo Identifier   │  151090FD-69E8-44B3-AB56-FB38904…  │   │
│  │ Camera Type        │  Back Wide Angle                    │   │
│  │ Acceleration Vec   │  0.0049  -0.8415  -0.5269           │   │
│  └──────────────────┴───────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. ExifToolGui — Metadatos IMG_0004.MOV

```
┌─────────────────────────────────────────────────────────────────┐
│              ExifToolGui 5.16.0.0                               │
│              File: IMG_0004.MOV                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Duration         │  2.50 seconds                               │
│  Resolution       │  1440 × 1080                                │
│  Codec            │  HEVC (hvc1)                                │
│  Capture Date     │  2024-02-14 16:21:03 UTC                    │
│  Device           │  Apple iPad (8th generation)                │
│  Rotation         │  90°                                        │
│  Content ID       │  9EDD30F4-9E7B-4B3D-B9F0-16EA96BCC1F5     │
│  GPS              │  [Not present]                              │
│                                                                  │
│  ⚠ Content ID matches IMG_0004.HEIC → Same Live Photo event    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. ExifToolGui — Metadatos IMG_0005.PNG

```
┌─────────────────────────────────────────────────────────────────┐
│              ExifToolGui 5.16.0.0                               │
│              File: IMG_0005.PNG                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  File Type        │  PNG — Screenshot                           │
│  Resolution       │  1620 × 2160                                │
│  File Size        │  4.5 MB                                     │
│  Capture Date     │  2024-12-04 15:00:13                        │
│  Orientation      │  Horizontal                                 │
│  Content Type     │  Screenshot                                  │
│  GPS              │  [Not present]                              │
│                                                                  │
│  ┌── Visual Content ────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  ╔═══════════════════════════════════════════════════╗   │   │
│  │  ║  ¿Confiar en este ordenador?                     ║   │   │
│  │  ║  Tus ajustes y datos estarán accesibles desde    ║   │   │
│  │  ║  este ordenador si se conectan de forma          ║   │   │
│  │  ║  inalámbrica o usando un cable.                  ║   │   │
│  │  ║                                                 ║   │   │
│  │  ║        [ Confiar ]    [ No confiar ]             ║   │   │
│  │  ╚═══════════════════════════════════════════════════╝   │   │
│  │                                                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9. DB Browser for SQLite — Photos.sqlite (Deleted Media Check)

```
┌─────────────────────────────────────────────────────────────────┐
│              DB Browser for SQLite 3.13.1                       │
│              File: Photos.sqlite                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌── Table: ZADDITIONALASSETATTRIBUTES ─────────────────────┐   │
│  │                                                          │   │
│  │  Z_PK │ ZPTPTRASHEDSTATE  │ Meaning                      │   │
│  │ ──────┼───────────────────┼────────────────────────────── │   │
│  │   1   │  0                │ ✅ Normal (not deleted)       │   │
│  │   2   │  0                │ ✅ Normal (not deleted)       │   │
│  │   3   │  0                │ ✅ Normal (not deleted)       │   │
│  │                                                          │   │
│  │  ZPTPTRASHEDSTATE: 0=Normal  1=Recently Deleted  2=Purged │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌── Table: ZGENERICALBUM ─────────────────────────────────┐   │
│  │                                                          │   │
│  │  All albums have ZTRASHEDSTATE = 0                       │   │
│  │  All albums have ZTRASHEDDATE = [NULL]                   │   │
│  │                                                          │   │
│  │  → No albums were deleted. No "Recently Deleted" album.  │   │
│  │                                                          │   │
│  │  ZTRASHEDSTATE: 0=Normal  1=Trash  2=Permanently Deleted │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌── Table: ZASSET ────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  Z_PK │ ZTRASHEDSTATE │ ZVISIBILITYSTATE                 │   │
│  │ ──────┼───────────────┼─────────────────────────────────  │   │
│  │   1   │  0            │  0 (visible)                     │   │
│  │   2   │  0            │  0 (visible)                     │   │
│  │   3   │  0            │  0 (visible)                     │   │
│  │                                                          │   │
│  │  → No files deleted, hidden, or in trash                 │   │
│  │                                                          │   │
│  │  ZTRASHEDSTATE: 0=Normal  1=Recently Deleted  2=Purged    │   │
│  │  ZVISIBILITYSTATE: 0=Visible  1=Hidden  2=Not visible    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 10. iBackup Viewer — Keychain (Encrypted)

```
╔══════════════════════════════════════════════════════════════════╗
║                    iBackup Viewer 1.6.4.90                      ║
║                    Keychain Manager                             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  Keychain File: keychain-backup.plist                           ║
║  Encryption:    AES-GCM/CCM                                     ║
║  Status:        🔒 Locked (password required)                    ║
║                                                                  ║
║  ┌── Encrypted Entries ─────────────────────────────────────┐   ║
║  │  Entry 1: com.apple.accounts                             │   ║
║  │  Entry 2: com.apple.mail                                 │   ║
║  │  Entry 3: com.apple.icloud                               │   ║
║  │  Entry 4: com.apple.safari                               │   ║
║  │  Entry 5: ... (15 entries total)                         │   ║
║  │                                                          │   ║
║  │  ⚠ Cannot decrypt — master password required             │   ║
║  └──────────────────────────────────────────────────────────┘   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 11. DB Browser for SQLite — sms.db (Empty)

```
┌─────────────────────────────────────────────────────────────────┐
│              DB Browser for SQLite 3.13.1                       │
│              File: sms.db                                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Table: message                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  No rows returned. (0 records)                          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Table: chat                                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  No rows returned. (0 records)                          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Table: chat_message_join                                        │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  No rows returned. (0 records)                          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Table: chat_handle_join                                         │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  No rows returned. (0 records)                          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Table: sync_deleted_chats                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  No rows returned. (0 records)                          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ✓ All tables confirmed empty                                   │
│  ✓ No deleted messages found                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 12. DB Browser for SQLite — CallHistory.storedata (Empty)

```
┌─────────────────────────────────────────────────────────────────┐
│              DB Browser for SQLite 3.13.1                       │
│              File: CallHistory.storedata                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Table: ZCALLRECORD                                              │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  No rows returned. (0 records)                          │    │
│  │                                                         │    │
│  │  ⚠ transactions.log also empty                           │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 13. iBackup Viewer — Contactos (Empty)

```
╔══════════════════════════════════════════════════════════════════╗
║                    iBackup Viewer 1.6.4.90                      ║
║                    Contacts Manager                             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ┌── Contacts List ─────────────────────────────────────────┐   ║
║  │                                                          │   ║
║  │  📇 No contacts found in AddressBook.sqlitedb            │   ║
║  │                                                          │   ║
║  │  Table ABPerson:             0 records                   │   ║
║  │  Table ABPersonChanges:      0 records (no modifications)│   ║
║  │  Table ABPersonMultiValue…:  0 records (no deletions)    │   ║
║  │                                                          │   ║
║  └──────────────────────────────────────────────────────────┘   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 14. iBackup Viewer — Notas

```
╔══════════════════════════════════════════════════════════════════╗
║                    iBackup Viewer 1.6.4.90                      ║
║                    Notes Export                                 ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ┌── Note #1 ──────────────────────────────────────────────┐   ║
║  │                                                          │   ║
║  │  Title:    PRUEBA JUAN JOSÉ ESPI                         │   ║
║  │  Created:  2024-02-14 17:21:50                           │   ║
║  │  Content:  [Empty]                                       │   ║
║  │                                                          │   ║
║  └──────────────────────────────────────────────────────────┘   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 15. DB Browser for SQLite — interactionC.db (Empty)

```
┌─────────────────────────────────────────────────────────────────┐
│              DB Browser for SQLite 3.13.1                       │
│              File: interactionC.db                              │
│              Path: mobile/Library/CoreDuet/People               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Table: ZINTERACTIONS                                            │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  No rows returned. (0 records)                          │    │
│  │                                                         │    │
│  │  → No user interaction records found                    │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 16. iBackup Viewer — Aplicaciones Instaladas

```
╔══════════════════════════════════════════════════════════════════╗
║                    iBackup Viewer 1.6.4.90                      ║
║                    Installed Apps                               ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ┌── System Apps ──────────────────────────────────────────┐   ║
║  │  • Settings                                              │   ║
║  │  • Safari                                                │   ║
║  │  • Photos                                                │   ║
║  │  • Camera                                                │   ║
║  │  • Notes                                                 │   ║
║  │  • Contacts                                              │   ║
║  │  • Phone                                                 │   ║
║  │  • Messages                                              │   ║
║  │  • FaceTime                                              │   ║
║  │  • App Store                                             │   ║
║  └──────────────────────────────────────────────────────────┘   ║
║                                                                  ║
║  ┌── Third-Party Apps ─────────────────────────────────────┐   ║
║  │  ⚠ No third-party applications found                    │   ║
║  │  ⚠ No social media apps installed                       │   ║
║  └──────────────────────────────────────────────────────────┘   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```
