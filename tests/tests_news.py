"""
Teste simples do modelo News.

Este arquivo demonstra como criar e utilizar um objeto da classe News.

Acesse o terminal na raiz do projeto e execute: python -m tests.tests_news
"""

from src.models.news import News


def main() -> None:
    """
    Executa um teste simples da classe News.
    """

    noticia = News(
        title="Python 3.12 é lançado",
        url="https://python.org"
    )

    print(noticia)
    print(f"Título : {noticia.title}")
    print(f"URL    : {noticia.url}")


if __name__ == "__main__":
    main()