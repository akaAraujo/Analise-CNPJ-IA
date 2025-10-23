import re
import json
from pathlib import Path


def validate_cnpj(cnpj: str) -> bool:
    """Valida o formato do CNPJ."""
    if not cnpj:
        return False
    cnpj = clean_cnpj(cnpj)
    return len(cnpj) == 14


def clean_cnpj(cnpj: str) -> str:
    """Remove caracteres não numéricos do CNPJ."""
    return re.sub(r"[^\d]", "", cnpj)


def load_cnae_json():
    # Carrega o arquivo JSON contendo os CNAEs permitidos.
    current_dir = Path(__file__).resolve().parent
    json_file_path = current_dir.parent / "data" / "cnae_permitidos.json"

    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            dados_cnae = json.load(file)
            return dados_cnae

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar o arquivo JSON de CNAEs permitidos: {e}")
        return []


def imprime_dict(dicionario: dict) -> None:
    # Imprime um dicionário de forma formatada.
    for chave, valor in dicionario["analise"].items():
        print(f"{chave}: {valor}")
    print('------------------------------')
