import requests

print("=== Meu primeiro script em Python ===")

#Chamando um API pública (github)
r = requests.get("https://api.github.com")
if r.status_code == 200:
    print("Conexão bem-sucedida!")
    print("Chaves do JSON recebido:", list(r.json().keys()))
else:
    print("Erro:", r.status_code)