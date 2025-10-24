import requests
import json
from utils import clean_cnpj


def consulta_cnpj(cnpj: str):
    data_dict = {}

    # Consulta informações do CNPJ utilizando a API da Open CNPJ
    cnpj = clean_cnpj(cnpj)
    url = f"https://api.opencnpj.org/{cnpj}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("A requisição foi bem-sucedida.")

        data_dict = json.loads(response.text)

        return data_dict

    # Caso a requisição não seja bem-sucedida, uma exceção será lançada
    except requests.exceptions.RequestException as e:

        if response.status_code == 404:
            print(
                f"Erro na requisição: {response.status_code} - CNPJ não encontrado.")
            raise ValueError("CNPJ não encontrado.")

        elif response.status_code == 429:
            print(
                f"Erro na requisição: {response.status_code} - Limite de requisições atingido.")
            raise ValueError(
                "Limite de requisições atingido. Tente novamente mais tarde.")
        else:
            print(f"Ocorreu um erro na requisição: {e}")
            raise ValueError("Erro ao consultar o CNPJ.")
