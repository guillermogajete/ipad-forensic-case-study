# Teoria Media Ipad

Aquí tienes una explicación clara y profesional de cada tabla que aparece en tu captura:

Tabla

Descripción breve

ACHANGE

Registro interno de cambios (CoreData). No contiene fotos.

ATRANSACTION

Transacciones internas de la base de datos. No contiene fotos.

ATRANSACTIONSTRING

Cadenas asociadas a transacciones. No contiene fotos.

ZADDITIONALASSETATTRIBUTES

Atributos adicionales de cada foto/vídeo (incluye ZTRASHEDSTATE, ZTRASHEDDATE). Clave para detectar borrados.

ZALBUMLIST

Lista de álbumes del usuario (incluye “Eliminado”, “Favoritos”, etc.).

ZASSET

La tabla principal: cada foto y vídeo del dispositivo. Incluye tipo, fecha, flags, etc.

ZASSETANALYSISSTATE

Estado del análisis de IA (caras, escenas, etc.).

ZASSETDESCRIPTION

Descripciones generadas por IA (no siempre presente).

ZCLOUDFEEDENTRY

Entradas de iCloud Photos (sincronización).

ZCLOUDMASTER

Identificadores de fotos en iCloud.

ZCLOUDMASTERMEDIAMETADATA

Metadatos de fotos en iCloud.

ZCLOUDRESOURCE

Recursos asociados a fotos en iCloud (miniaturas, originales).

ZCLOUDSHAREDALBUMINVITATIONRECORD

Invitaciones a álbumes compartidos.

ZCLOUDSHAREDCOMMENT

Comentarios en álbumes compartidos.

ZCODEC

Información sobre codecs de vídeo.

ZCOMPUTEDASSETATTRIBUTES

Atributos calculados (clasificación, IA, etc.).

ZDEFERREDBUILDFACE

Caras pendientes de procesar.

ZDETECTEDFACE

Caras detectadas en fotos.

ZDETECTEDFACEGROUP

Grupos de caras.

ZDETECTEDFACEPRINT

Huellas faciales (vectores).

ZEXTENDEDATTRIBUTES

Atributos extendidos de fotos.

ZFACECROP

Recortes de caras.

ZFILESYSTEMBOOKMARK

Referencias a archivos en el sistema.

ZFILESYSTEMVOLUME

Información de volúmenes.

ZGENERICALBUM

Álbumes del usuario (incluye “Eliminado recientemente”).

ZGLOBALKEYVALUE

Configuración interna.

ZINTERNALRESOURCE

Recursos internos de fotos.

ZKEYWORD

Palabras clave asignadas a fotos.

ZLEGACYFACE

Caras antiguas (formatos previos).

Z_METADATA

Metadatos de CoreData.

Z_MODELCACHE

Caché del modelo de IA.

Z_PRIMARYKEY

Control interno de claves.

Estas son las que sí debes revisar para saber si hay fotos/vídeos borrados y para obtener información útil:

Tabla

Por qué es importante

ZASSET

Lista completa de fotos y vídeos.

ZADDITIONALASSETATTRIBUTES

Indica si una foto/vídeo está borrado (ZTRASHEDSTATE, ZTRASHEDDATE).

ZGENERICALBUM

Permite identificar el álbum “Recently Deleted”.

ZALBUMLIST

Relación entre álbumes y fotos.

ZCLOUDMASTER

Si hay sincronización con iCloud Photos.

ZCLOUDRESOURCE

Si hay fotos en iCloud aunque no estén en el dispositivo.

Campos clave:

ZTRASHEDSTATE

0 = normal

1 = movido a “Eliminado recientemente”

2 = eliminado permanentemente

ZPTPTRASHEDSTATE

Fecha en la que se eliminó

Busca álbum con:

ZKIND = 2 → “Recently Deleted”

Si tiene elementos → hubo fotos borradas.

Campos útiles:

ZDELETERECORD

ZVISIBILITYSTATE

ZCLOUDDELETIONSTATE

Ejemplo:

1, 2, 3, 7, 8, 9 → faltan 4, 5, 6 → fotos eliminadas.

Tabla origen

Relación

Tabla destino

Explicación

ZASSET

1:1

ZADDITIONALASSETATTRIBUTES

Atributos extendidos (incluye borrados).

ZASSET

N:1

ZGENERICALBUM

Relación foto ↔ álbum.

ZASSET

1:N

ZCLOUDRESOURCE

Recursos en iCloud.

ZASSET

1:N

ZDETECTEDFACE

Caras detectadas.

ZGENERICALBUM

1:N

ZALBUMLIST

Estructura de álbumes.

Aquí tienes un texto profesional:

Se analizó la base de datos Photos.sqlite, que contiene la información completa de las fotografías y vídeos del dispositivo, incluyendo metadatos, álbumes, atributos extendidos y sincronización con iCloud.

Las tablas relevantes para el análisis forense fueron ZASSET, ZADDITIONALASSETATTRIBUTES, ZGENERICALBUM y ZALBUMLIST.

La tabla ZADDITIONALASSETATTRIBUTES permite identificar elementos eliminados mediante los campos ZTRASHEDSTATE y ZTRASHEDDATE. La tabla ZGENERICALBUM permite verificar si existieron elementos en el álbum “Eliminado recientemente”.

(Aquí añades tus conclusiones: si hay o no fotos borradas.)