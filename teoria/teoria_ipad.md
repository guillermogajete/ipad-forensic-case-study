# Teoria Ipad

Sumario

2. ZACCOUNTTYPE4

3. ZACCOUNTPROPERTY4

4. ZAUTHORIZATION4

5. ZCREDENTIALITEM4

6. ZDATACLASS5

❌ TABLAS NO IMPORTANTES (por qué NO se usan en forense)5

❌ ZACCESSOPTIONSKEY5

❌ Z_1OWNINGACCOUNTTYPES5

❌ Z_ZENABLEDATACLASSES5

❌ Z_ZPROVISIONEDDATACLASSES5

❌ Z_4SUPPORTEDDATACLASSES5

❌ Z_4SYNCABLEDATACLASSES5

❌ Z_METADATA, Z_MODELCACHE, Z_PRIMARYKEY5

Media5

Información5

Lo que NO te ayuda a saber si se borraron fotos:6

PhotoData6

1. Journals6

📁 2. MISC6

📁 3. private7

📁 4. Thumbnails7

📄 5. Photos.sqlite7

📄 6. protection7

📄 7. suspendnebulad8

Photos.sqlite8

1. ZASSET8

2. ZADDITIONALASSETATTRIBUTES8

3. ZGENERICALBUM8

4. ZASSETCOLLECTION9

5. ZDELETEDASSET (si existe)9

6. ZCLOUDMASTER / ZCLOUDASSET9

🟥 ❌ Tablas que NO sirven para análisis forense9

🟩 ✔ CAMPOS RELEVANTES DE ZASSET (solo los que importan en forense)9

✅ 1. ZDIRECTORY10

✅ 2. ZFILENAME10

✅ 3. ZDATECREATED10

✅ 4. ZTRASHEDSTATE10

✅ 5. ZTRASHEDDATE10

✅ 6. ZUUID10

✅ 7. ZWIDTH / ZHEIGHT11

✅ 8. ZUNIFORMTYPEIDENTIFIER11

Información sobre Account3.sqlite

Ruta

Se encuentra en System > mobile > Library > Accounts > VerifiedBackup

Tablas

Nombre

Qué es / Para qué sirve

ZACCESSOPTIONSKEY

Opciones de acceso de las cuentas (ajustes técnicos sobre cómo se usan).

ZACCOUNT

Tabla principal de cuentas del dispositivo (Apple ID, iCloud, etc.).

ZACCOUNTPROPERTY

Propiedades adicionales de cada cuenta (nombre visible, flags, ajustes).

ZACCOUNTTYPE

Tipos de cuenta (iCloud, Mail, Calendario, etc.). Se relaciona con ZACCOUNT.

ZAUTHORIZATION

Información sobre autorizaciones/permisos de las cuentas (si están autorizadas, estado).

ZCREDENTIALITEM

Elementos de credenciales cifradas (tokens, claves de sesión). No hay contraseñas en claro.

ZDATACLASS

Tipos de datos que maneja una cuenta (contactos, mail, calendarios, notas…).

Z_1OWNINGACCOUNTTYPES

Tabla de relación entre cuentas y tipos de cuenta. Técnica, de enlace.

Z_ZENABLEDATACLASSES

Relación entre cuentas y clases de datos habilitadas (qué sincroniza cada cuenta).

Z_ZPROVISIONEDDATACLASSES

Relación entre cuentas y clases de datos “provisionadas” (configuradas para usarse).

Z_4SUPPORTEDDATACLASSES

Qué tipos de datos soporta cada tipo de cuenta.

Z_4SYNCABLEDATACLASSES

Qué tipos de datos se pueden sincronizar para cada cuenta.

Z_METADATA

Metadatos internos de Core Data. No contiene información útil de usuario.

Z_MODELCACHE

Caché del modelo de datos. Interno, no relevante para el análisis.

Z_PRIMARYKEY

Gestión de claves primarias internas. Tampoco contiene datos de cuentas.

1. ZACCOUNT (IMPRESCINDIBLE)

Qué contiene:

Las cuentas configuradas en el dispositivo

Apple ID

Cuentas de correo

Servicios iCloud asociados

Identificadores de usuario

Fechas de creación/modificación

Por qué es importante: Es la tabla que demuestra qué cuentas reales estaban en el dispositivo. Es la que te da puntos en tu informe.

Qué contiene:

El tipo de cada cuenta (iCloud, Gmail, Calendarios, etc.)

Por qué es importante: Permite interpretar correctamente ZACCOUNT. Sin esta tabla, no sabes si un registro es un Apple ID, un calendario o un servicio interno.

Qué contiene:

Propiedades adicionales de cada cuenta

Flags

Ajustes

Información de estado

Por qué es importante: Ayuda a confirmar si una cuenta estaba activa, verificada o configurada.

Qué contiene:

Estado de autorización de cada cuenta

Si está validada

Si requiere autenticación

Por qué es importante: Sirve para demostrar si la cuenta estaba operativa en el dispositivo.

Qué contiene:

Tokens cifrados

Claves de sesión

Información de autenticación

Por qué es importante: Aunque no contiene contraseñas, demuestra que la cuenta estaba logueada y tenía credenciales válidas.

Qué contiene:

Qué datos sincroniza cada cuenta (contactos, mail, notas, calendarios…)

Por qué es importante: Permite saber qué información del usuario dependía de cada cuenta.

Estas tablas no aportan información útil del usuario, solo estructura interna de Apple.

Opciones internas de acceso. No contiene datos del usuario.

Son tablas de relación entre cuentas y tipos de datos. No contienen información identificable del usuario. Solo sirven para que iOS sepa qué sincronizar.

Tablas internas de CoreData. No contienen datos del usuario. Nunca se usan en análisis forense.

Ruta

System > mobile > Media > DCIM

DCIM/100APPLE → Contiene las fotos y vídeos originales. Si faltan números (ejemplo: IMG_0001, IMG_0002, IMG_0004 → falta el 0003), es indicio de eliminación.

Thumbnails/V2/DCIM/100APPLE → Contiene miniaturas. Si hay miniaturas de fotos que NO están en DCIM, es prueba de que existieron y se borraron.

PhotoData → Aquí se guardan bases de datos internas del carrete. Si hay referencias a fotos que ya no existen, también indica borrado.

MediaAnalysis

Recordings

private/com.apple.accountsd

private/com.apple.assetsd

private/com.apple.mobileslideshow

Son registros de cambios de la base de datos Photos.sqlite.

Sirven para:

Reconstruir modificaciones

Ver cambios recientes

A veces recuperar referencias a fotos eliminadas

👉 Forense: útil.

Carpeta con archivos auxiliares del sistema Fotos.

Incluye:

Configuraciones

Datos temporales

Archivos de soporte

👉 Forense: poco útil, salvo casos muy específicos.

Carpeta interna con subcarpetas de servicios del sistema:

com.apple.accountsd → gestión de cuentas

com.apple.assetsd → gestión de fotos y vídeos

com.apple.mobileslideshow → app Fotos

Aquí puede haber:

Metadatos

Referencias a fotos antiguas

Archivos que no se borran aunque la foto sí

👉 Forense: útil, especialmente assetsd.

Miniaturas de fotos y vídeos.

Si aquí aparece una miniatura de una foto que no está en DCIM, significa:

➡️ La foto existió y fue borrada.

👉 Forense: MUY útil.

La base de datos principal del carrete.

Contiene:

Lista de fotos y vídeos

Rutas

Fechas

Metadatos

Referencias a archivos eliminados

Información de álbumes

👉 Forense: la más importante de todas.

Archivo interno de seguridad.

No contiene fotos ni metadatos relevantes.

👉 Forense: no útil.

Archivo interno del sistema relacionado con procesos de fotos.

👉 Forense: no útil.

Estas son las que un analista forense revisa sí o sí:

La tabla más importante.

Contiene:

Cada foto y vídeo del carrete

Fecha de creación

Fecha de modificación

Ruta del archivo

Tipo (foto, vídeo, live photo, burst…)

Flags de borrado

Identificador único (ZUUID)

👉 Aquí se detectan fotos borradas.

Metadatos extendidos:

Nombre original del archivo

Hash

Duración del vídeo

Información de Live Photos

Datos EXIF (parciales)

👉 Muy útil para reconstruir información.

Lista de álbumes:

Carrete

Favoritos

Eliminados recientemente

Álbumes creados por el usuario

👉 Permite saber si una foto estuvo en “Eliminado recientemente”.

Relación entre fotos y álbumes.

👉 Sirve para saber si una foto estaba en un álbum concreto.

En algunas versiones aparece.

👉 Lista de fotos borradas.

Si el dispositivo usa iCloud Fotos:

Fotos sincronizadas

Fotos descargadas

Fotos solo en la nube

Fotos borradas en la nube

👉 Muy útil para saber si algo se borró desde iCloud.

(pero aparecen en la base de datos)

Z_METADATA

Z_PRIMARYKEY

Z_MODELCACHE

Tablas de relación internas

Tablas de caché

👉 No contienen datos del usuario.

Voy a centrarme en lo que realmente sirve para:

detectar fotos borradas

identificar fotos existentes

ver fechas

ver rutas

ver tipos de archivo

Ejemplo:

DCIM/100APPLE

Indica la carpeta donde está guardada la foto.

👉 Si una foto fue borrada, no aparece aquí.

Ejemplos:

IMG_0004.HEIC

IMG_0005.PNG

Los nombres de archivo del carrete.

👉 Si faltan números (ej: 0001, 0002, 0003, 0005), puede indicar borrado. En tu caso solo hay 0004 y 0005, así que no hay huecos previos.

Ejemplo:

729620462.8618364

755013613

Formato Apple Absolute Time (segundos desde 2001).

Sirve para saber cuándo se tomó la foto.

En tus dos registros está en 0.

Significado:

0 = no está en la papelera

1 o 2 = eliminada recientemente

👉 Tus fotos no están eliminadas.

En tus registros está vacío.

👉 No hay fecha de borrado → no hay fotos borradas.

Identificador único de cada foto.

Ejemplos:

832842A6-C2F2-4F67-A255-ED8326EE5901

BCEA08E4-78CE-43D0-948E-8AC343D2967F

Sirve para relacionar con otras tablas (atributos, miniaturas, etc.).

Resolución de la imagen.

Ejemplos:

3264 × 2448

2160 × 1620

Ejemplos:

public.heic

public.png

Indica el tipo de archivo.