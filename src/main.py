from connections import consulta_cnpj
from utils import validate_cnpj, imprime_dict
from empresa import Empresa
from connections_ia import analista_ia
from analise import analisar_CNPJ


def processar_cnpj(cnpj_input) -> None:
    # Função que executa o fluxo completo de processamento do CNPJ
    # Valida o CNPJ antes de fazer a consulta
    if not validate_cnpj(cnpj_input):
        raise ValueError("CNPJ inválido")

    # Realiza a consulta do CNPJ utilizando a função consulta_cnpj definida em connections.py
    resultado = consulta_cnpj(cnpj_input)
    # Realiza a criação do objeto Empresa definida em empresa.py
    empresa = Empresa(resultado)

    # Realiza a análise do CNPJ utilizando a função analisar_CNPJ definida em analise.py
    analise = analisar_CNPJ(empresa.dict_analise)

    if analise.get("status_preliminar") == "Reprovado":
        print("CNPJ Rejeitado:")
        imprime_dict(analise)
    elif analise.get("status_preliminar") == "Aprovado":
        print("CNPJ Aprovado:")
        imprime_dict(analise)
    elif analise.get("status_preliminar") == "Atenção":
        print("CNPJ em Atenção:")
        imprime_dict(analise)
        print("\nIniciando análise avançada com IA...")
        # Realiza a análise do CNPJ utilizando a função analisar_CNPJ definida em connections_ia.py
        analista_ia(analise, empresa.dict_analise)


def main() -> None:
    # Solicita ao usuário que insira o CNPJ para consulta
    cnpj_input = input("Digite o CNPJ para consulta: ")

    try:
        processar_cnpj(cnpj_input)

    except ValueError as e:
        print(f"\nOcorreu um erro durante o processamento do CNPJ: {e}")


if __name__ == "__main__":
    main()
