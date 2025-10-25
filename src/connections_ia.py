import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


def analista_ia(analise: dict, dados_empresa: dict) -> None:

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
        ANALISTA DE RISCO AI:
        Avalie o risco de crédito desta empresa para um produto financeiro educacional. A triagem inicial marcou a empresa como 'Atenção', a análise inicial retornou o dados: {analise}.
        Utilize os seguintes dados para uma análise aprofundada:

        FATOS ENCONTRADOS (TRIAGEM ESTRUTURADA):
            - Tempo de Atividade: {dados_empresa.get('idade_empresa')} anos
            - Capital Social: {dados_empresa.get('capital_social')}
            - CNAE Principal: {dados_empresa.get('cnae_principal')} (Compatível com educação, mas pode ser genérico)

        ANÁLISE SEMÂNTICA DISPONÍVEL (Nomes):
            - Razão Social: "{dados_empresa.get('razao_social')}"
            - Nome Fantasia: "{dados_empresa.get('nome_fantasia')}"

        Instrução:
        1. Análise Semântica: O Nome Fantasia e a Razão Social sugerem claramente uma atividade educacional (ex: 'Instituto', 'Escola', 'Treinamentos') ou são vagos/incompatíveis (ex: 'Logística', 'Importação', 'Construção')?
        2. Ponderação de Risco: Pese os riscos (como baixo tempo de atividade) contra os pontos positivos (capital social ou nome muito específico de educação).
        3. Retorne APENAS informações essências para a tomada de decisão.

        # Exemplo de Saída (Obrigatoriamente JSON):
        {{
        "Veredicto final": "[Aprovado|Reprovado|Atenção]",
        "Resultado da analise": "Apesar do Capital Social ser positivo, o Tempo de Atividade é inferior a 2 anos (risco). Além disso, o Nome Fantasia é muito genérico ('Serviços LTDA'), o que levanta dúvidas sobre o foco educacional mesmo com o CNAE compatível. Não Aprovado automaticamente."
        }}
    """

    try:
        resposta = cliente.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        print(resposta.text)
        print("-------------------------")

    except Exception as e:
        print(f"Erro ao gerar conteúdo com o modelo Gemini: {e}")
