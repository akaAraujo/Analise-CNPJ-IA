import re 

def validate_cnpj(cnpj: str) -> bool:
    """Valida o formato do CNPJ."""
    if not cnpj:
        return False
    cnpj = clean_cnpj(cnpj)
    return len(cnpj) == 14

def clean_cnpj(cnpj: str) -> str:
    """Remove caracteres não numéricos do CNPJ."""
    return re.sub(r"[^\d]", "", cnpj)
