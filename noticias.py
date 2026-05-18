from constantes import CLASSIFICACOES_VALIDAS
from repositorio import repositorio_noticias

def adicionar_noticia(
    titulo: str,
    classificacao: str = "duvidosa"
) -> bool:
    """
    Valida e adiciona uma nova notícia ao repositório.

    Critérios de validação:
    - O título não pode estar vazio.
    - A classificação deve ser reconhecida pelo sistema.

    Args:
        titulo (str): título da notícia.
        classificacao (str): classificação da notícia (default duvidosa).

    Returns:
        bool:
            True caso a notícia seja cadastrada com sucesso.
            False caso ocorra erro de validação.
    """

    titulo = titulo.strip()
    classificacao = classificacao.strip().lower()

    if not titulo:
        print("[Erro] O título da notícia não pode ser vazio.")
        return False

    if classificacao not in CLASSIFICACOES_VALIDAS:
        print("[Erro] Classificação inválida.")
        return False

    noticia = {
        "titulo": titulo,
        "classificacao": classificacao
    }

    repositorio_noticias.append(noticia)

    print("[Sucesso] Notícia cadastrada.")
    return True

def exibir_lista_noticias():
    """
    Exibe todas as notícias cadastradas no repositório.
    """

    if not repositorio_noticias:
        print("\n--- Nenhuma notícia cadastrada ---")
        return

    print("\n--- Lista de Notícias ---")

    for i, noticia in enumerate(repositorio_noticias, start=1):

        print(f"{i}. Título: {noticia['titulo']}")
        print(
            f"   Classificação: {noticia['classificacao'].capitalize()}"
        )
        print("-" * 30)