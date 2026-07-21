"""
Módulo responsável por definir o modelo de dados de uma notícia.

Toda notícia encontrada pelos scrapers será representada por um
objeto da classe News.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class News:
    """
    Representa uma notícia encontrada durante o processo de Web Scraping.

    Attributes
    ----------
    title : str
        Título da notícia.

    url : str
        Endereço completo da notícia.
    """

    title: str
    url: str