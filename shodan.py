import shodan
import os
from dotenv import load_dotenv

load_dotenv()
 
opciones = {
           "test.com" : "specific_info"
            }
 
API_KEY = os.getenv("SECRET")

print(API_KEY)  
 
for org, title in opciones:
    query = f"org:'{org}'" + f" http.html:'control'"  
    print(query)
 
    api = shodan.Shodan(API_KEY)
 
    try:
        results = api.search(query)
 
        print(f"{results['total']} results were found.\n")
 
        for result in results['matches']:
            ip = result['ip_str']
            port = result['port']
            hostnames = ", ".join(result.get('hostnames', [])) or "N/A"
            
            print(f"{ip}:{port} - Hostnames: {hostnames}")
            
            with open("output.txt", "a") as f:
                f.write(f"{ip}:{port} - Hostnames: {hostnames}\n")
 
    except shodan.APIError as e:
        print(f"API Error: {e}")