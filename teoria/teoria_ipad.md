## Teoría y Metodología: Extracción de Artefactos (Accounts, Media, Photos.sqlite)

Este documento detalla la estructura lógica de bases de datos críticas adicionales en entornos iPadOS/iOS, centrándose en la gestión de cuentas y la evidencia multimedia.

## 1. Gestión de Cuentas: Accounts3.sqlite

* **Ruta:** `System > mobile > Library > Accounts > VerifiedBackup` (Nota: La ruta estándar operativa suele ser `/private/var/mobile/Library/Accounts/Accounts3.sqlite`).

### 1.1 Tablas Relevantes para Análisis Forense

| Tabla | Descripción | Relevancia Forense |
| :--- | :--- | :--- |
| `ZACCOUNT` | Tabla principal de cuentas configuradas (Apple ID, correos, iCloud). | Imprescindible |
| `ZACCOUNTTYPE` | Define el protocolo/servicio de la cuenta. | Crítica |
| `ZACCOUNTPROPERTY` | Propiedades adicionales, flags, estado de verificación. | Importante |
| `ZAUTHORIZATION` | Estado de autorización/permisos (validación y autenticación). | Importante |
| `ZCREDENTIALITEM` | Tokens cifrados y claves de sesión (demuestra inicio de sesión). | Útil |
| `ZDATACLASS` | Tipos de datos sincronizados (contactos, mail, calendarios). | Útil |

### 1.2 Tablas NO Relevantes (Estructura Interna)
Las siguientes tablas carecen de valor probatorio directo y gestionan la estructura interna de la base de datos o preferencias de sincronización del sistema operativo:
* `ZACCESSOPTIONSKEY`
* `Z_1OWNINGACCOUNTTYPES`
* `Z_ZENABLEDATACLASSES`
* `Z_ZPROVISIONEDDATACLASSES`
* `Z_4SUPPORTEDDATACLASSES`
* `Z_4SYNCABLEDATACLASSES`
* `Z_METADATA`, `Z_MODELCACHE`, `Z_PRIMARYKEY`

## 2. Evidencia Multimedia: Estructura de Carpetas

El análisis de la carpeta `Media` es fundamental para la recuperación de imágenes y la identificación de borrados.

* **Ruta Base:** `System > mobile > Media`

### Directorios Críticos

* **`DCIM`:** Contiene subcarpetas (ej. `100APPLE`) con los archivos originales (`.HEIC`, `.PNG`, `.MOV`). Saltos en la secuencia de nombres (ej. `IMG_0001`, `IMG_0003`) pueden sugerir eliminación.
* **`PhotoData`:** Aloja bases de datos internas del carrete, incluyendo `Photos.sqlite` y registros de cambios (Journals). Referencias a archivos inexistentes indican borrado.
* **`Thumbnails`:** Especialmente útil. Las miniaturas almacenadas (ej. `Thumbnails/V2/DCIM/100APPLE`) persisten a menudo tras el borrado del archivo original, sirviendo como prueba gráfica de su existencia.
* **`private`:** Contiene subcarpetas de servicios (`com.apple.assetsd`, `com.apple.mobileslideshow`). `assetsd` es particularmente relevante para metadatos o rastros residuales.

*Nota: Carpetas como `MISC`, y archivos como `protection` o `suspendnebulad` carecen, por norma general, de utilidad en el análisis forense estándar.*

## 3. Análisis de Photos.sqlite

Base de datos central para la gestión del carrete fotográfico.

* **Ruta:** `System > mobile > Media > PhotoData > Photos.sqlite`

### 3.1 Tablas Clave para Análisis Forense

| Tabla | Descripción | Relevancia Forense |
| :--- | :--- | :--- |
| `ZASSET` | Registro principal de cada archivo multimedia (ruta, fechas, tipo, estado de borrado). | Imprescindible |
| `ZADDITIONALASSETATTRIBUTES` | Metadatos extendidos (nombre original, hash, datos EXIF parciales). | Importante |
| `ZGENERICALBUM` | Lista de álbumes, incluyendo "Eliminado recientemente". | Importante |
| `ZASSETCOLLECTION` | Relación para determinar en qué álbumes específicos residía un archivo. | Útil |
| `ZDELETEDASSET` | Si está presente, proporciona un listado directo de archivos borrados. | Útil |
| `ZCLOUDMASTER` / `ZCLOUDASSET` | Información sobre el estado de sincronización con iCloud Fotos. | Útil |

*(Las tablas internas de metadatos, cachés y primary keys como `Z_METADATA` deben descartarse para la extracción de evidencia).*

### 3.2 Campos Críticos de la Tabla ZASSET

Para auditar la existencia, ubicación y estado de eliminación de un archivo multimedia, se deben priorizar los siguientes atributos dentro de `ZASSET`:

* **`ZDIRECTORY`:** Ruta del directorio donde se aloja el archivo (ej. `DCIM/100APPLE`).
* **`ZFILENAME`:** Nombre del archivo (ej. `IMG_0004.HEIC`).
* **`ZDATECREATED`:** Fecha de creación en formato *Mac Absolute Time* (requiere conversión).
* **`ZTRASHEDSTATE`:** Indicador de borrado. `0` = Normal; `1` o `2` = Eliminado recientemente.
* **`ZTRASHEDDATE`:** Fecha en la que el archivo fue enviado a la papelera. Si está vacío o nulo, el archivo no ha sido eliminado mediante procesos estándar.
* **`ZUUID`:** Identificador único global. Crucial para realizar *joins* con otras tablas (ej. `ZADDITIONALASSETATTRIBUTES`).
* **`ZWIDTH` / `ZHEIGHT`:** Resolución nativa de la imagen.
* **`ZUNIFORMTYPEIDENTIFIER`:** Define el tipo MIME/UTI del archivo (ej. `public.heic`, `public.png`).
