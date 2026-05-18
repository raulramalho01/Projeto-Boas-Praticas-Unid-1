def classificar_texto_automaticamente(texto: str) -> str:
    """
    Analisa o conteúdo do texto e define automaticamente
    uma classificação de risco.

    Critérios utilizados:
    - Uso de "!!!"
    - Uso da palavra "URGENTE"
    - Texto muito curto

    Retorna:
        str: confiável, duvidosa ou falsa
    """

    pontuacao_risco = 0

    if "!!!" in texto:
        pontuacao_risco += 1

    if "URGENTE" in texto.upper():
        pontuacao_risco += 1

    if len(texto.strip()) < 10:
        pontuacao_risco += 1

    if pontuacao_risco == 0:
        return "confiavel"

    if pontuacao_risco == 1:
        return "duvidosa"

    return "falsa"