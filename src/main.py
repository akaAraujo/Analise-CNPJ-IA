from connections import consulta_cnpj
from utils import validate_cnpj
from empresa import Empresa
from connections_ia import analisar_CNPJ


if __name__ == "__main__":
    cnpj_input = input("Digite o CNPJ para consulta: ")

    # Valida o CNPJ antes de fazer a consulta
    if not validate_cnpj(cnpj_input):
        raise ValueError("CNPJ inválido")

    # Realiza a consulta do CNPJ utilizando a função consulta_cnpj definida em connections.py
    resultado = consulta_cnpj(cnpj_input)

    # Realiza a criação do objeto Empresa definida em empresa.py se o resultado não for None
    empresa = Empresa(resultado)

    
 