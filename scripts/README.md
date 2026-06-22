# Forensic Scripts

Scripts Python desarrollados para el análisis forense del iPad 14.

---

## decodificar_nskeyed_es.py

Decodificador forense universal para valores `ZVALUE` de la tabla `ZACCOUNTPROPERTY` en `Accounts3.sqlite`.

### Formatos soportados

- Base64
- Plist binario
- NSKeyedArchiver (resolución de referencias UID)
- Strings
- Booleanos
- Fechas Apple Absolute Time → UTC / Local
- Arrays y diccionarios

### Uso

```bash
# Pasar el valor Base64 como argumento
python decodificar_nskeyed_es.py "YnBsaXN0MDDUAQIDBAU..."

# O pegarlo interactivamente
python decodificar_nskeyed_es.py
```

### Ejemplo de salida

```
DECODIFICADOR FORENSE UNIVERSAL ZVALUE
======================================================================

VALOR REAL DECODIFICADO:
{'primaryEmail': 'xxxxxx@gmail.com', 'primaryAccount': True,
 'firstName': 'xxxx', 'lastName': 'xxxx', 'regionInfo': 'España',
 'personID': '211xxxxx', 'usesCloudDocs': True}

✔ Decodificación completada
```

### Dependencias

- `Python 3.x`
- `plistlib` (librería estándar)
- `base64` (librería estándar)

---

## buscar_cuentas.py

Busca patrones forenses en archivos XML exportados del keychain de iOS.

### Funcionalidad

- Busca direcciones de correo electrónico mediante regex
- Identifica servicios/apps (iCloud, Gmail, Apple, etc.)
- Extrae posibles nombres de usuario y etiquetas de cuenta
- Guarda resultados en `resultados_busqueda.txt`

### Uso

```bash
python buscar_cuentas.py
```

Por defecto busca en `pass.plist.xml`. Para usar otro archivo, modificar la llamada en la línea:

```python
buscar_cuentas_forense("pass.plist.xml")
```

### Ejemplo de salida

```
============================================================
 CORREOS ELECTRÓNICOS ENCONTRADOS:
============================================================
  xxxxxxxi@gmail.com

============================================================
 SERVICIOS/APP IDENTIFICADAS:
============================================================
  🔹 Apple
  🔹 iCloud

============================================================
 POSIBLES USUARIOS/NOMBRES DE CUENTA:
============================================================
  👤 xxxxxx

[+] Resultados guardados en: resultados_busqueda.txt
```

### Dependencias

- `Python 3.x`
- `re` (librería estándar)
- `os` (librería estándar)

---

## Notas

- Los scripts están diseñados para entornos forenses controlados
- No modifican los archivos de entrada
- Las fechas Apple Absolute Time se convierten usando el epoch `9xxxxxxxx` (1/1/2001)
