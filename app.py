import requests
import json

# Chave de API obtida no site da OpenAI
API_KEY = "sua_api_key_aqui"

# URL da API do OpenAI para completar o chat
API_URL = "https://api.openai.com/v1/chat/completions"

# Cabeçalhos necessários para autenticação na API
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def obter_ideias_startup():
    # Solicita informações do usuário
    nome = input('Digite seu nome: ')
    print(f"Olá, {nome}.\nVou te auxiliar para ter algumas ideias de startups.")
    experiencia = input("Quais são suas experiências ou habilidades? ")
    investimento = int(input("Qual seria o valor que você poderia investir? "))

    # Monta a mensagem para enviar à API
    mensagem_usuario = f"""Meu nome é: {nome} e minhas experiências são: {experiencia}.
                        Tenho o valor de {investimento}. Poderia me fornecer ideias de startup."""

    # Corpo da mensagem em formato JSON
    corpo_mensagem = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": mensagem_usuario}]
    }

    # Converte o corpo da mensagem para JSON
    corpo_mensagem_json = json.dumps(corpo_mensagem)

    # Faz a solicitação à API do OpenAI
    resposta = requests.post(API_URL, headers=headers, data=corpo_mensagem_json)

    # Verifica se a solicitação foi bem-sucedida
    if resposta.status_code == 200:
        # Extrai a mensagem da resposta JSON
        mensagem_resposta = resposta.json()["choices"][0]["message"]["content"]
        print("Ideias de startup sugeridas:")
        print(mensagem_resposta)
    else:
        print("Erro ao obter ideias de startup. Status code:", resposta.status_code)

# Chamada da função principal
obter_ideias_startup()


