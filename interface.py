from noticias import (
    adicionar_noticia,
    exibir_lista_noticias
)

from classificacao import (
    classificar_texto_automaticamente
)

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