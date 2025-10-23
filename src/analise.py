from utils import load_cnae_json


# Status que levam à Reprovação Direta
STATUS_REPROVACAO_DIRETA = {"SUSPENSA", "BAIXADA", "INAPTA"}

cnae_permitidos = load_cnae_json()


def analisar_CNPJ(dados_cnpj: dict) -> dict:

    analise = {}

    # Analise do CNAE principal da empresa, caso esteja fora da lista de CNAEs permitidos retorna reprovado.
    # Caso esteja na lista, é retornado a aprovação.
    cnae_principal = dados_cnpj.get("cnae_principal", "")
    if cnae_principal not in cnae_permitidos:
        analise["motivo_reprovacao"] = f"CNAE principal '{cnae_principal}' não condizente com a operação de educação."
        return {"status_preliminar": "Reprovado", "analise": analise}
    else:
        analise["cnae_principal"] = f"CNAE principal '{cnae_principal}' condizente com a operação de educação."

    # Analise da situação cadastral da empresa, caso esteja entre os status de reprovação direta retorna reprovado.
    # Caso contrário, adiciona a situação cadastral na análise como positiva.
    situacao = dados_cnpj.get("situacao_cadastral", "").upper()
    if situacao in STATUS_REPROVACAO_DIRETA:
        analise["motivo_reprovacao"] = f"Empresa com situação cadastral '{situacao}'"
        return {"status_preliminar": "Reprovado", "analise": analise}
    else:
        analise["situacao_cadastral"] = f"Positivo, empresa com situação cadastral '{situacao}'"

    # Caso a empresa passe pelas analises preliminares ela segue para a próxima etapa de análise.
    pontos_positivos = 0
    pontos_atencao = 0

    # Analise do tempo de atividade da empresa
    # Caso a empresa tenha 2 anos ou mais de atividade, soma 1 ponto positivo, caso contrário soma 1 ponto de atenção.
    tempo_atividade = dados_cnpj.get("idade_empresa", 0)
    if tempo_atividade >= 2:
        pontos_positivos += 1
        analise["tempo_atividade"] = f"Positivo, empresa com {tempo_atividade} anos de atividade."
    else:
        pontos_atencao += 1
        analise["tempo_atividade"] = f"Atenção, empresa com {tempo_atividade} anos de atividade."

    # Analise do capital social da empresa
    # Caso o capital social seja igual ou maior que R$ 100.000,00 soma 1 ponto positivo, caso contrário soma 1 ponto de atenção.
    capital_social = dados_cnpj.get("capital_social", 0)
    if capital_social >= 100000:
        pontos_positivos += 1
        analise["capital_social"] = f"Positivo, capital social de R$ {capital_social:.2f}."
    else:
        pontos_atencao += 1
        analise["capital_social"] = f"Atenção, capital social de R$ {capital_social:.2f}."

    # Resultado da análise preliminar
    # Caso a empresa tenha somado apenas pontos positivos, retorna aprovado.
    if pontos_positivos >= 2 and pontos_atencao == 0:
        status_final = "Aprovado"
    # Caso a empresa possua algum ponto de atenção, retorna atenção (necessita de análise).
    elif pontos_positivos > 0 and pontos_atencao >= 1:
        status_final = "Atenção"
    else:
        status_final = "Atenção"

    return {"status_preliminar": status_final, "analise": analise}
