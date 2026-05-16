"""
Sistema de Monitoramento de Fake News e Qualidade da Informação.

O sistema permite:
- Cadastro manual de notícias
- Classificação automática
- Listagem das notícias cadastradas
"""

# Repositório que armazena as notícias
repositorio_noticias = []

# Classificações aceitas
CLASSIFICACOES_VALIDAS = {
    "confiavel",
    "duvidosa",
    "falsa"
}

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
        titulo -- título da notícia.
        classificacao -- classificação da notícia (default duvidosa).

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


def tratar_entrada_manual():
    """
    Realiza o cadastro manual de uma notícia.
    """

    titulo = input("Digite o título da notícia: ")

    print(
        "Opções disponíveis: "
        "confiavel, duvidosa, falsa"
    )

    classe = input(
        "Digite a classificação "
        "(pressione Enter para padrão): "
    ).strip()

    if not classe:
        adicionar_noticia(titulo)
        return

    adicionar_noticia(titulo, classe)


def tratar_entrada_automatica():
    """
    Realiza o cadastro com classificação automática.
    """

    titulo = input(
        "Digite o título da notícia: "
    )

    if not titulo.strip():
        print("[Erro] Texto inválido.")
        return

    classificacao = classificar_texto_automaticamente(titulo)

    adicionar_noticia(titulo, classificacao)

    print(
        f"Classificação automática atribuida: {classificacao.upper()}"
    )


def menu_principal():
    """
    Controla o fluxo principal do sistema.
    """

    opcoes = {
        "1": tratar_entrada_manual,
        "2": tratar_entrada_automatica,
        "3": exibir_lista_noticias,
        "4": exit
    }

    while True:

        print("\nSISTEMA DE MONITORAMENTO DE NOTÍCIAS")
        print("1. Adicionar Manualmente")
        print("2. Adicionar com Análise Automática")
        print("3. Listar Notícias")
        print("4. Sair")

        escolha = input("Selecione uma opção: ")

        acao = opcoes.get(escolha)

        if not acao:
            print("[Erro] Opção inválida.")
            continue

        if escolha == "4":
            print("Encerrando sistema...")
            break

        acao()

if __name__ == "__main__":
    menu_principal()