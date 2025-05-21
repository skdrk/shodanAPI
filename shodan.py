import shodan
import os
from dotenv import load_dotenv

load_dotenv()
 
opciones = {
           "test.com" : "info_especifica"
            }
 
API_KEY = os.getenv("SECRET")

print(API_KEY)  
 
for org, title in opciones.items():
    query = f"org:'{org}'" + f" http.html:'control'"  
    print(query)
 
    api = shodan.Shodan(API_KEY)
 
    try:
        results = api.search(query)
 
        print(f"Se encontraron {results['total']} resultados.\n")
 
        for result in results['matches']:
            ip = result['ip_str']
            port = result['port']
            hostnames = ", ".join(result.get('hostnames', [])) or "N/A"
            
            print(f"{ip}:{port} - Hostnames: {hostnames}")
            
            with open("resultados.txt", "a") as f:
                f.write(f"{ip}:{port} - Hostnames: {hostnames}\n")
 
    except shodan.APIError as e:
        print(f"Error en la API: {e}")