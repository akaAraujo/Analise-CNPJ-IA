from datetime import datetime

class Empresa:
    def __init__(self, data: dict):
        self.__razao_social = data.get("razao_social")
        self.__nome_fantasia = data.get("nome_fantasia")
        self.__cnpj = data.get("cnpj")
        self.__situacao_cadastral = data.get("situacao_cadastral")
        self.__data_inicio_atividade = data.get("data_inicio_atividade")
        self.__cnae_principal = data.get("cnae_principal")
        self.__capital_social = float(data.get("capital_social", 0).replace(',', '.'))

    # Propriedades para acessar os atributos da empresa de forma segura

    @property
    def razao_social(self) -> str:
        return self.__razao_social
    
    @property
    def nome_fantasia(self) -> str:
        return self.__nome_fantasia
    
    @property
    def cnpj(self) -> str:
        return self.__cnpj
    
    @property
    def situacao_cadastral(self) -> str:
        return self.__situacao_cadastral
    
    @property
    def cnae_principal(self) -> str:
        return self.__cnae_principal
    
    @property
    def capital_social(self) -> float:
        return self.__capital_social
    
    @property
    def idade_empresa(self) -> int:
        # Calcula a idade da empresa em anos.
        if not self.__data_inicio_atividade:
            return 0
        inicio_atividade = datetime.strptime(self.__data_inicio_atividade, "%Y-%m-%d")
        hoje = datetime.today()
        idade = hoje.year - inicio_atividade.year - ((hoje.month, hoje.day) < (inicio_atividade.month, inicio_atividade.day))
        return idade

    @property
    def dict_analise (self) -> dict:
        # Retorna um dicionário com os dados da empresa para análise.
        return {
            "razao_social": self.razao_social,
            "nome_fantasia": self.nome_fantasia,
            "cnpj": self.cnpj,
            "situacao_cadastral": self.situacao_cadastral,
            "cnae_principal": self.cnae_principal,
            "capital_social": self.capital_social,
            "idade_empresa": self.idade_empresa
        }