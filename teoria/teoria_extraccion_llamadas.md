## Teoría y Metodología: Extracción de Historial de Llamadas

Este documento detalla la estructura lógica de la base de datos de llamadas en entornos iPadOS/iOS, enfocándose en la identificación de registros de comunicaciones y la interpretación de hallazgos negativos.

## 1. Ruta del Artefacto
* **Archivo:** `CallHistory.storedata`
* **Ruta:** `/private/var/mobile/Library/CallHistoryDB/CallHistory.storedata`

## 2. Análisis de Tablas Principales

La integridad de la extracción depende de la correcta interpretación de las tablas contenidas en la base de datos.

| Tabla | Contenido | Importancia |
| :--- | :--- | :--- |
| `ZCALLRECORD` | Llamadas (entrantes, salientes, perdidas) | Imprescindible |
| `ZCALLRECORDMETADATA` | Detalles extendidos (duración, flags) | Importante |
| `ZCONTACT` | Vínculos con la agenda (si aplica) | Opcional |
| `ZFACE` | Registros de llamadas FaceTime | Situacional |
| `Z_METADATA` | Versión del esquema y sincronización | Documentación |



## 3. Interpretación de Hallazgos y Resultados

En caso de que las tablas `ZCALLRECORD` y `ZCALLRECORDMETADATA` no contengan registros, es imperativo realizar una verificación de consistencia antes de declarar el historial como inexistente.

## 4. Declaración para Informe Pericial (Hallazgo Negativo)

> "Tras el análisis técnico de la base de datos `CallHistory.storedata`, se concluye que el dispositivo no contiene registros de llamadas en el historial local. No se han identificado llamadas entrantes, salientes, perdidas ni registros de FaceTime. La estructura de la base de datos se confirma vacía."

## 5. Posibles Causas Justificadas

* **Gestión del Usuario**: Eliminación manual del historial de llamadas.
* **Estado del Dispositivo**: Restauración a valores de fábrica o dispositivo nuevo sin uso previo para llamadas.
* **Sincronización iCloud**: El historial de llamadas está sincronizado exclusivamente con la nube y no posee persistencia local en el almacenamiento del iPad.
* **Uso de Dispositivo**: Ausencia de uso del dispositivo para servicios de telefonía o FaceTime.

## 6. Consideraciones Avanzadas

Solo en casos de sospecha de borrado intencional o corrupción de datos, se recomienda proceder con una reconstrucción avanzada. Sin embargo, para un informe forense estándar, el análisis de las tablas principales es suficiente para certificar la ausencia de evidencia.
