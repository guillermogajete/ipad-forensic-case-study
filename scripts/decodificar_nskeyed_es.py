#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Decodificador Forense Universal para ZVALUE (iOS/macOS)
Compatible con:
 - Base64
 - Plist binario
 - NSKeyedArchiver (resolución de UID)
 - Strings
 - Booleanos
 - Fechas Apple Absolute Time (UTC + Local)
 - Arrays y diccionarios

Autor: Guillermo (versión final)
"""

import base64
import plistlib
import datetime
import sys
from plistlib import UID
from typing import Any

APPLE_EPOCH = 978307200  # Offset Apple → Unix


# ------------------------------------------------------------
# 🔧 Conversión de fechas Apple Absolute Time
# ------------------------------------------------------------
def convertir_fecha_apple(valor: Any):
    """Convierte fechas Apple Absolute Time a UTC y Local."""
    try:
        if isinstance(valor, (int, float)):
            unix = valor + APPLE_EPOCH
            dt_utc = datetime.datetime.fromtimestamp(unix, datetime.UTC)
            dt_local = dt_utc.astimezone()  # Zona local del sistema
            return {
                "utc": dt_utc.isoformat(),
                "local": dt_local.isoformat()
            }
    except:
        pass
    return None


# ------------------------------------------------------------
# 🔧 Resolver UID(n) → objects[n]
# ------------------------------------------------------------
def resolver_uid(obj, objects):
    """Resuelve UID(n) → objects[n] recursivamente."""
    if isinstance(obj, UID):
        return resolver_uid(objects[obj.data], objects)

    if isinstance(obj, dict):
        return {k: resolver_uid(v, objects) for k, v in obj.items()}

    if isinstance(obj, list):
        return [resolver_uid(x, objects) for x in obj]

    return obj


# ------------------------------------------------------------
# 🔧 Procesar cualquier tipo de objeto plist
# ------------------------------------------------------------
def procesar_objeto(obj: Any):
    """Interpreta cualquier tipo de objeto plist."""
    # Booleanos
    if isinstance(obj, bool):
        return obj

    # Números → posible fecha Apple
    if isinstance(obj, (int, float)):
        fecha = convertir_fecha_apple(obj)
        return fecha if fecha else obj

    # Strings
    if isinstance(obj, str):
        return obj

    # Arrays
    if isinstance(obj, list):
        return [procesar_objeto(x) for x in obj]

    # Diccionarios
    if isinstance(obj, dict):
        return {k: procesar_objeto(v) for k, v in obj.items()}

    # NSData → intentar extraer texto
    if isinstance(obj, bytes):
        try:
            return obj.decode("utf-8", errors="ignore")
        except:
            return obj.hex()

    return obj


# ------------------------------------------------------------
# 🔧 Decodificación principal
# ------------------------------------------------------------
def decodificar_zvalue(b64_input: str):
    print("\n" + "="*70)
    print("🔍 DECODIFICADOR FORENSE UNIVERSAL ZVALUE")
    print("="*70)

    # 1. Base64
    try:
        raw = base64.b64decode(b64_input)
    except Exception as e:
        print(f"❌ Error Base64: {e}")
        return

    # 2. Intentar plist
    try:
        plist = plistlib.loads(raw)
    except Exception:
        print("⚠️ No es un plist válido. Intentando extraer texto…")
        texto = raw.decode("utf-8", errors="ignore")
        print("\n📄 TEXTO EXTRAÍDO:")
        print(texto)
        return

    # 3. Si es NSKeyedArchiver → resolver UID
    if isinstance(plist, dict) and "$objects" in plist and "$top" in plist:
        objects = plist["$objects"]
        root = plist["$top"]["root"]
        valor_real = resolver_uid(root, objects)
        valor_real = procesar_objeto(valor_real)

        print("\n📌 VALOR REAL DECODIFICADO:")
        print(valor_real)

    else:
        # Plist normal
        resultado = procesar_objeto(plist)
        print("\n📌 RESULTADO DECODIFICADO:")
        print(resultado)

    print("\n" + "="*70)
    print("✔ Decodificación completada")
    print("="*70 + "\n")


# ------------------------------------------------------------
# 🔧 Entrada por consola
# ------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
    else:
        print("📋 Pega aquí el contenido Base64 de ZVALUE:")
        entrada = input("> ").strip()

    decodificar_zvalue(entrada)
