from datetime import datetime

class Empresa:
    def __init__(self, data: dict):
        self.__razao_social = data.get("razao_social")
        self.__cnpj = data.get("cnpj")
        self.__situacao_cadastral = data.get("situacao_cadastral")
        self.__data_inicio_atividade = data.get("data_inicio_atividade")
        self.__cnae_principal = data.get("cnae_principal")
        self.__capital_social = float(data.get("capital_social", 0).replace(',', '.'))

    @property
    def idade_empresa(self) -> int:
        # Calcula a idade da empresa em anos.
        if not self.__data_inicio_atividade:
            return 0
        inicio_atividade = datetime.strptime(self.__data_inicio_atividade, "%Y-%m-%d")
        hoje = datetime.today()
        idade = hoje.year - inicio_atividade.year - ((hoje.month, hoje.day) < (inicio_atividade.month, inicio_atividade.day))
        return idade