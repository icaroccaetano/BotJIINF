import requests

url = 'https://jiinf-api.vercel.app/api/v1/times/atualizar_pontos/12/'
headers = {
    'Content-Type': 'application/json',
    'Origin': 'https://www.unificada.com'
}

for i in range(10000):
    response = requests.post(url, headers=headers)
    print(response.status_code)  # Opcional, para verificar o status de cada requisição
