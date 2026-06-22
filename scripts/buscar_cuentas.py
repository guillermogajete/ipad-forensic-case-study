import os
import re

def buscar_cuentas_forense(xml_file):
    print(f"[*] Realizando búsqueda forense en: {xml_file}")
    
    if not os.path.exists(xml_file):
        print(f"[!] Error: No encuentro {xml_file}")
        return

    # Leer el archivo como texto crudo para buscar patrones
    try:
        with open(xml_file, 'rb') as f:
            raw_data = f.read()
        
        # Decodificar ignorando errores para poder buscar con regex
        text_data = raw_data.decode('utf-8', errors='ignore')
        
    except Exception as e:
        print(f"[!] Error al leer: {e}")
        return

    print("[*] Escaneando patrones de correos y servicios...")
    
    # 1. Buscar emails con regex
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text_data)
    
    # 2. Buscar servicios conocidos
    servicios_pattern = r'(icloud|gmail|google|apple|facebook|microsoft|outlook|yahoo|hotmail)[a-zA-Z0-9._-]*'
    servicios = re.findall(servicios_pattern, text_data, re.IGNORECASE)
    
    # 3. Buscar posibles usuarios/nombres cerca de etiquetas
    user_pattern = r'(?:acct|username|user|label)[=:]\s*["\']?([a-zA-Z0-9._@-]+)["\']?'
    users = re.findall(user_pattern, text_data, re.IGNORECASE)

    # Mostrar resultados
    print("\n" + "="*60)
    print(" CORREOS ELECTRÓNICOS ENCONTRADOS:")
    print("="*60)
    if emails:
        for email in sorted(set(emails)):
            print(f"  ✅ {email}")
    else:
        print("  ❌ No se encontraron emails explícitos.")

    print("\n" + "="*60)
    print(" SERVICIOS/APP IDENTIFICADAS:")
    print("="*60)
    if servicios:
        for svc in sorted(set(servicios)):
            print(f"  🔹 {svc}")
    else:
        print("  ❌ No se identificaron servicios.")

    print("\n" + "="*60)
    print("👤 POSIBLES USUARIOS/NOMBRES DE CUENTA:")
    print("="*60)
    if users:
        for user in sorted(set(users)):
            print(f"  👤 {user}")
    else:
        print("  ❌ No se encontraron usuarios explícitos.")

    # Guardar en archivo
    output_file = "resultados_busqueda.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("RESULTADOS DE BÚSQUEDA FORENSE - KEYCHAIN\n")
        f.write("="*60 + "\n\n")
        f.write("CORREOS ENCONTRADOS:\n")
        for email in sorted(set(emails)):
            f.write(f"  - {email}\n")
        f.write("\nSERVICIOS IDENTIFICADOS:\n")
        for svc in sorted(set(servicios)):
            f.write(f"  - {svc}\n")
        f.write("\nUSUARIOS ENCONTRADOS:\n")
        for user in sorted(set(users)):
            f.write(f"  - {user}\n")
    
    print(f"\n[+] Resultados guardados en: {output_file}")

if __name__ == "__main__":
    buscar_cuentas_forense("pass.plist.xml")