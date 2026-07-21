"""
Teste simples do módulo de constantes.

Para testar abra o terminal e execute na raiz do projeto: python -m tests.tests_constants 
"""

from src.core.constants import (
    DEFAULT_HEADERS,
    DEFAULT_TIMEOUT,
    DEFAULT_USER_AGENT,
)


def main() -> None:
    """
    Exibe os valores das constantes definidas no projeto.
    """

    print(f"Timeout padrão : {DEFAULT_TIMEOUT} segundos")
    print(f"User-Agent     : {DEFAULT_USER_AGENT}")
    print(f"Cabeçalhos     : {DEFAULT_HEADERS}")


if __name__ == "__main__":
    main()