import os
from dotenv import load_dotenv
from google import genai
from google.genai import types



def analisar_CNPJ():

    # Carregar variáveis de ambiente do arquivo .env
    load_dotenv()

    # API KEY configurada através de variável de ambiente GOOGLE_API_KEY
    try:

        cliente = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    except Exception as e:
        print(f"Erro ao criar o cliente GenAI: {e}")
        exit(1)

    # Modelo de prompt para a análise de CNPJ
    dados_CNPJ = """Como fritar um ovo?"""

    try:
        resposta = cliente.models.generate_content(
            model="gemini-2.5-flash",
            contents=dados_CNPJ
        )

        print("Resposta do modelo Gemini:")
        print(resposta.text)
        print("-------------------------")

        print(f"Tokens entrada: {resposta.usage_metadata.prompt_token_count}")
        print(f"Tokens saída: {resposta.usage_metadata.candidates_token_count}" )
    
    except Exception as e:
        print(f"Erro ao gerar conteúdo com o modelo Gemini: {e}")
