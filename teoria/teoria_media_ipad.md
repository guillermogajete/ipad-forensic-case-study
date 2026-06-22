## Teoría y Metodología: Análisis de Media en iPadOS

Este documento detalla la estructura extendida de la base de datos multimedia en dispositivos Apple, centrándose en la identificación de activos gráficos, análisis de metadatos de IA, sincronización en la nube y detección de elementos eliminados.

## 1. Análisis Estructural de Tablas (Photos.sqlite)

La base de datos contiene un gran volumen de tablas. A continuación, se clasifican según su función técnica y relevancia para la pericial.

| Tabla | Descripción Técnica | Relevancia Forense |
| :--- | :--- | :--- |
| `ZASSET` | Tabla principal: cada foto y vídeo del dispositivo. | Crítica |
| `ZADDITIONALASSETATTRIBUTES` | Atributos extendidos (incluye marcadores de borrado). | Crítica |
| `ZGENERICALBUM` | Álbumes del usuario (incluye la papelera "Eliminado recientemente"). | Crítica |
| `ZALBUMLIST` | Estructura y lista de álbumes del usuario. | Importante |
| `ZCLOUDMASTER` | Identificadores de fotos sincronizadas en iCloud. | Importante |
| `ZCLOUDRESOURCE` | Recursos asociados a fotos en iCloud (miniaturas, originales). | Importante |
| `ZCLOUDFEEDENTRY` | Entradas de sincronización con iCloud Photos. | Opcional |
| `ZCLOUDSHARED*` | Tablas relacionadas con álbumes compartidos y comentarios. | Opcional |
| `ZASSETANALYSISSTATE` | Estado del análisis de IA local (caras, escenas). | Opcional |
| `ZDETECTEDFACE*` | Huellas faciales, grupos y caras detectadas en fotos. | Opcional |
| `ACHANGE` / `ATRANSACTION*` | Registros y transacciones internas de CoreData. | Sin relevancia |
| `Z_METADATA` / `Z_PRIMARYKEY` | Metadatos y control de claves de SQLite. | Sin relevancia |



## 2. Metodología para la Detección de Borrados

Para determinar si existen fotografías o vídeos eliminados, el análisis debe centrarse en los siguientes campos y comportamientos del sistema.

### Indicadores en ZADDITIONALASSETATTRIBUTES
* **`ZTRASHEDSTATE`**: Identifica el estado del archivo.
    * `0` = Normal (Activo).
    * `1` = Movido a "Eliminado recientemente".
    * `2` = Eliminado permanentemente (Purgado).
* **`ZPTPTRASHEDSTATE` / `ZTRASHEDDATE`**: Registra el *timestamp* exacto en el que el elemento fue enviado a la papelera.

### Indicadores en ZGENERICALBUM
* **Búsqueda por `ZKIND`**: El valor `ZKIND = 2` corresponde al álbum del sistema "Recently Deleted" (Eliminado recientemente). Si este álbum contiene elementos o un recuento mayor a cero, existe evidencia de borrado.

### Otros campos de control útiles:
* `ZDELETERECORD`
* `ZVISIBILITYSTATE`
* `ZCLOUDDELETIONSTATE`

### Análisis de Secuencia de Archivos (Carrete)
* La alteración en la nomenclatura secuencial de los archivos en la carpeta `DCIM` es un fuerte indicio de borrado físico.
* *Ejemplo:* Si los registros muestran `IMG_0001`, `IMG_0002`, `IMG_0003`, `IMG_0007`, `IMG_0008`; la ausencia de los identificadores `4, 5 y 6` evidencia la eliminación de dichos archivos.

## 3. Relaciones Lógicas entre Tablas Multimedia

Para reconstruir el historial o ubicación de un archivo multimedia, se deben ejecutar los siguientes *joins*:

| Tabla Origen | Relación | Tabla Destino | Explicación |
| :--- | :--- | :--- | :--- |
| `ZASSET` | 1:1 | `ZADDITIONALASSETATTRIBUTES` | Conecta la foto con sus atributos extendidos y estado de borrado. |
| `ZASSET` | N:1 | `ZGENERICALBUM` | Identifica a qué álbum o álbumes pertenece una foto. |
| `ZASSET` | 1:N | `ZCLOUDRESOURCE` | Vincula el archivo local con sus copias/recursos en iCloud. |
| `ZASSET` | 1:N | `ZDETECTEDFACE` | Conecta la imagen con el análisis biométrico de rostros. |
| `ZGENERICALBUM` | 1:N | `ZALBUMLIST` | Reconstruye la jerarquía y estructura de los álbumes. |

## 4. Declaración para Informe Pericial

*Este bloque está redactado para ser incluido directamente en la sección de metodología o conclusiones del dictamen pericial:*

> "Se procedió al análisis técnico de la base de datos `Photos.sqlite`, la cual aloja la estructura principal de los activos multimedia (fotografías y vídeos) del dispositivo, abarcando metadatos, estructuración de álbumes, atributos extendidos y el estado de sincronización con el servicio iCloud.
>
> Para este análisis forense, se auditaron de manera prioritaria las tablas `ZASSET`, `ZADDITIONALASSETATTRIBUTES`, `ZGENERICALBUM` y `ZALBUMLIST`. Específicamente, la evaluación de la tabla `ZADDITIONALASSETATTRIBUTES` permitió verificar el estado de eliminación de los activos a través de los marcadores `ZTRASHEDSTATE` y `ZTRASHEDDATE`. Asimismo, la inspección de la tabla `ZGENERICALBUM` facilitó la comprobación de la existencia y contenido del contenedor temporal 'Eliminado recientemente'."
>
> **[Insertar conclusión específica del caso: Ej. Tras dicho análisis, se concluye la inexistencia de registros marcados como eliminados...]**
