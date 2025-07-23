from instagrapi import Client
import time
import random
from datetime import datetime, timedelta

# Tus credenciales de Instagram
username = 'fiorellajazmin222'
password = 'CamiLo222'

# Conexión al cliente de Instagram
cl = Client()
cl.login(username, password)

# URL del Reel donde vas a comentar
reel_url = "https://www.instagram.com/reel/DMYp8dBS7QQ/?igsh=eDQwbDJmN2E0d3Nq"

# Obtener el media ID (identificador de la publicación)
media_id = cl.media_pk_from_url(reel_url)

# Comentario que vas a hacer
comentario = "@camiloposik1 @manuelchiarlone @enzovaccaro4"

# Definir el tiempo de finalización: 17 días desde ahora
fin = datetime.now() + timedelta(days=17)

# Bucle para comentar cada minuto (aproximadamente, con random)
while datetime.now() < fin:
    try:
        cl.media_comment(media_id, comentario)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Comentario enviado.")
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error al comentar: {e}")
    
    # Espera aleatoria entre 60 y 80 segundos
    espera = random.randint(60, 80)
    print(f"Esperando {espera} segundos para el próximo comentario...")
    time.sleep(espera)