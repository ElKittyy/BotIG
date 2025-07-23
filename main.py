from instagrapi import Client
import time
import random
from datetime import datetime, timedelta
import os

# Si vas a usar variables de entorno locales (opcional)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # Si no se usa .env, no hay problema

# ✅ Credenciales desde entorno o directamente
username = os.getenv("IG_USERNAME", "tu_usuario_aqui")
password = os.getenv("IG_PASSWORD", "tu_contraseña_aqui")

# Conexión a Instagram
cl = Client()

try:
    cl.login(username, password)
    print("[+] Sesión iniciada correctamente.")
except Exception as e:
    print(f"[ERROR] Falló el login: {e}")
    exit()

# URL del Reel objetivo
reel_url = "https://www.instagram.com/reel/DMYp8dBS7QQ/?igsh=eDQwbDJmN2E0d3Nq"

try:
    media_id = cl.media_pk_from_url(reel_url)
except Exception as e:
    print(f"[ERROR] No se pudo obtener media_id desde la URL: {e}")
    exit()

# Comentario a realizar
comentario = "@fiorellajazmin1 @manuel.chiarlone @enzovaccaro4"

# Tiempo límite: 17 días desde ahora
fin = datetime.now() + timedelta(days=17)

print(f"[INFO] Bot activo hasta: {fin.strftime('%Y-%m-%d %H:%M:%S')}")
print("[INFO] Comenzando bucle de comentarios...")

# Bucle principal
while datetime.now() < fin:
    try:
        cl.media_comment(media_id, comentario)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Comentario enviado correctamente.")
    except Exception as e:
        print(f"[ERROR] Comentario fallido: {e}")
    
    # Espera aleatoria entre comentarios
    espera = random.randint(60, 80)
    print(f"[INFO] Esperando {espera} segundos...")
    time.sleep(espera)