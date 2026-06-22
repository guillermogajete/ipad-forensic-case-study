# Teoria Extraccion Cuentas

1. Cuentas en el dispositivo

Ruta principal: /private/var/mobile/Library/Accounts/Accounts3.sqlite.

1.1Accounts3.sqlite

1.2 Tabla ZACCOUNT

Tabla principal de cuentas del dispositivo (Apple ID, iCloud, etc.).

Campos

1. Los campos absolutamente imprescindibles:

ZUSERNAME: El más importante de todos. Aquí es donde encontrarás el dato real de la cuenta, como la dirección de correo electrónico (ej. usuario@gmail.com) o el ID de Apple.

ZACCOUNTDESCRIPTION: Es el nombre "amigable" o la etiqueta que el usuario (o el iPad automáticamente) le asignó a la cuenta. Te ayudará a contextualizar si dice "Trabajo", "iCloud", "Personal", etc.

ZACCOUNTTYPE: Es fundamental para cruzar datos. Contiene un número (una clave foránea) que deberás buscar en la tabla ZACCOUNTTYPE para saber exactamente de qué servicio se trata (CardDAV para contactos, CalDAV para calendarios, Exchange, IMAP, etc.).

2. Campos de alto valor para la investigación (Línea de tiempo y estado):

ZDATE: Marca de tiempo de cuándo se añadió o modificó la cuenta. Ojo con esto: como indican las fuentes respecto a otras bases de datos de Apple, estos tiempos suelen guardarse en formato Mac Absolute Time (segundos transcurridos desde el 1 de enero de 2001). Necesitarás convertir este valor para poner una fecha legible en tu informe.

ZACTIVE y ZAUTHENTICATED: Te indican (normalmente con un 1 para Sí y un 0 para No) si la cuenta está actualmente habilitada en el iPad y si el usuario ha iniciado sesión correctamente.

ZIDENTIFIER: Es un identificador único (GUID) de la cuenta. Si más adelante en tu análisis forense encuentras carpetas o archivos huérfanos con este código largo, sabrás que pertenecen exactamente a esta cuenta.

ZOWNINGBUNDLEID: Te mostrará el nombre del paquete de la aplicación responsable de gestionar esa cuenta (ej. com.apple.account.icloud).

Ruta secundaria (Info del dispositivo/Apple ID): /private/var/root/Library/Lockdown/data_ark.plist.

Pasos a seguir: Utiliza un visor de bases de datos SQLite para abrir el archivo Accounts3.sqlite. Aquí encontrarás un listado con todas las cuentas configuradas en el iPad, como el ID de Apple (iCloud), correos electrónicos (Gmail, Outlook, etc.) y cuentas de redes sociales.

Por qué podrías no encontrarlo: Si solo tienes acceso a una extracción básica (estado bloqueado BFU), es posible que los archivos estén cifrados. Además, si el usuario no vinculó correos en la app nativa de Apple y usó navegadores web, no aparecerán en esta base de datos.

2. Contraseñas de dichas cuentas

Ruta principal: /private/var/Keychains/keychain-2.db (conocido como el Llavero o Keychain de Apple).

Pasos a seguir: Debes realizar una "extracción del sistema de archivos completo (FFS)" que incluya la extracción específica del Keychain. Este archivo almacena contraseñas de Wi-Fi, cuentas de correo y tokens de acceso de aplicaciones.

Por qué podrías no encontrarlo (Justificación para el informe):

Cifrado severo: El llavero está protegido por el Secure Enclave del hardware de Apple. Si no posees el código de desbloqueo (PIN) del iPad, las claves de cifrado necesarias para leer este archivo no estarán disponibles en la memoria y será imposible descifrar las contraseñas.

Extracción lógica: Si el método que utilizaste fue una copia de seguridad normal de iTunes (sin contraseña de respaldo) o una extracción lógica simple, el sistema operativo de Apple bloquea por seguridad la exportación de las contraseñas.

3. Mensajes y llamadas

Rutas de aplicaciones nativas:

SMS e iMessage: /private/var/mobile/Library/SMS/sms.db (revisa las tablas message y handle).

Llamadas (FaceTime/Teléfono): /private/var/mobile/Library/CallHistoryDB/CallHistory.storedata.

Ruta de aplicaciones de terceros (WhatsApp, Skype, etc.): En iPadOS, las apps instaladas por el usuario se guardan en carpetas con nombres aleatorios (GUID).

Paso previo: Para saber en qué carpeta está la app que buscas, primero abre /private/var/mobile/Library/Caches/com.apple.mobile.installation.plist. Ahí verás a qué app corresponde cada carpeta.

Paso final: Ve a /private/var/mobile/Containers/Data/Application/<CARPETA_DE_LA_APP>/Documents/ y busca el archivo .sqlite principal (por ejemplo, ChatStorage.sqlite para WhatsApp).

Por qué podrías no encontrarlo (Justificación para el informe):

Borrados irrecuperables: Si el usuario borró los mensajes, la memoria Flash (NAND) del iPad ejecuta un proceso llamado "Recolección de basura" (Garbage Collection) que destruye los datos físicamente de forma muy rápida. A diferencia de los ordenadores antiguos, en los iPad modernos la recuperación de datos borrados es prácticamente imposible.

Restricción de Clase de Protección: Las bases de datos de mensajes y correos suelen tener "Protección Completa" (Clase A) o "Protección hasta la primera autenticación" (Clase C). Esto significa que si el iPad fue reiniciado y nadie introdujo el PIN (estado BFU), los mensajes están cifrados a nivel de sistema de archivos y no podrás leerlos.