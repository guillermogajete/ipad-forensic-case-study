## Teoría y Metodología: Extracción de Cuentas y Evidencias

Este documento describe la estructura lógica y la ubicación de los artefactos forenses críticos en entornos iPadOS, orientados a la extracción y análisis de cuentas de usuario, credenciales y comunicaciones.

## 1. Gestión de Cuentas en el Dispositivo

La persistencia de las cuentas configuradas se localiza principalmente en la base de datos de gestión de cuentas de Apple.

* **Ruta principal:** `/private/var/mobile/Library/Accounts/Accounts3.sqlite`

## 1.1. Análisis de la Tabla ZACCOUNT

Esta tabla constituye el núcleo de la identidad del usuario en el sistema.

### Campos de valor crítico:
* **ZUSERNAME**: Campo primario. Contiene el identificador de cuenta (ej. correo electrónico o Apple ID).
* **ZACCOUNTDESCRIPTION**: Etiqueta descriptiva asignada por el usuario o el sistema (ej. "iCloud", "Trabajo").
* **ZACCOUNTTYPE**: Clave foránea que referencia a la tabla ZACCOUNTTYPE. Es indispensable para determinar el protocolo de servicio (CardDAV, CalDAV, IMAP, Exchange).
* **ZDATE**: Timestamp en formato Mac Absolute Time (segundos desde el 01/01/2001). Requiere normalización para su inclusión en la cronología del informe.
* **ZACTIVE / ZAUTHENTICATED**: Indicadores booleanos (0/1) que validan el estado operativo de la cuenta.
* **ZIDENTIFIER**: GUID único. Vital para correlacionar archivos o directorios huérfanos con una cuenta específica.
* **ZOWNINGBUNDLEID**: Identificador del paquete (Bundle ID) de la aplicación que gestiona la cuenta (ej. com.apple.account.appleaccount).

## 2. Gestión de Credenciales (Keychain)

El Llavero de Apple almacena secretos, tokens de sesión y contraseñas.

* **Ruta principal:** `/private/var/Keychains/keychain-2.db`

### Consideraciones sobre la inaccesibilidad (Justificación Forense)
* **Cifrado vía Secure Enclave**: La integridad del Keychain está ligada al hardware. Sin el código de desbloqueo (PIN) del dispositivo, las claves maestras permanecen fuera del alcance, haciendo imposible la desencriptación.
* **Limitaciones de la Extracción**: Las extracciones lógicas o copias de seguridad estándar sin contraseña suelen omitir los datos sensibles del Keychain por políticas de seguridad del sistema operativo.

## 3. Mensajería y Comunicaciones

### 3.1. Aplicaciones Nativas
* **iMessage/SMS**: `/private/var/mobile/Library/SMS/sms.db` (Tablas: message, handle, chat).
* **Llamadas (FaceTime/Teléfono)**: `/private/var/mobile/Library/CallHistoryDB/CallHistory.storedata`.

### 3.2. Aplicaciones de Terceros (Sandbox)
El acceso a aplicaciones externas requiere una navegación por el árbol de directorios de contenedores:
1. **Mapeo**: Consultar `/private/var/mobile/Library/Caches/com.apple.mobile.installation.plist` para identificar el GUID de la aplicación.
2. **Acceso**: Dirigirse a `/private/var/mobile/Containers/Data/Application/<GUID>/Documents/` para localizar las bases de datos de usuario (ej. ChatStorage.sqlite en WhatsApp).

## 4. Consideraciones Técnicas y Limitaciones Forenses

Para garantizar la validez del informe, se deben incluir las siguientes justificaciones en caso de ausencia de hallazgos:

* **Procesos de Borrado (NAND Flash)**: En sistemas iPadOS modernos, el proceso de Garbage Collection y el comando TRIM eliminan físicamente los datos borrados, invalidando las técnicas clásicas de recuperación de bloques no asignados.
* **Clases de Protección de Archivos**: Las bases de datos críticas operan bajo clases de protección (Clase A o C). Si el dispositivo se encuentra en estado BFU (Before First Unlock), los archivos permanecen cifrados y son inaccesibles incluso con una extracción de sistema de archivos completo.
* **Acceso a Navegador**: Los datos no sincronizados con las aplicaciones nativas (mediante uso exclusivo de navegadores web) no se verán reflejados en las bases de datos de cuentas, limitando el rastro a historiales de navegación o cachés web.
