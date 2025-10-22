import os
from dotenv import load_dotenv
from google import genai
from google.genai import types



def analisar_CNPJ(analise: dict, dados_empresa : dict) -> None:

    # Carregar variáveis de ambiente do arquivo .env
    load_dotenv()

    # API KEY configurada através de variável de ambiente GOOGLE_API_KEY
    try:

        cliente = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    except Exception as e:
        print(f"Erro ao criar o cliente GenAI: {e}")
        exit(1)

    # Modelo de prompt para a análise de CNPJ
    # O prompt irá utilizar as informações da análise preliminar e os dados da empresa para gerar uma resposta.
    prompt = f"""
        
    """

    try:
        resposta = cliente.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("Resposta do modelo Gemini:")
        print(resposta.text)
        print("-------------------------")

        print(f"Tokens entrada: {resposta.usage_metadata.prompt_token_count}")
        print(f"Tokens saída: {resposta.usage_metadata.candidates_token_count}" )
    
    except Exception as e:
        print(f"Erro ao gerar conteúdo com o modelo Gemini: {e}")
