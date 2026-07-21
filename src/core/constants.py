"""
Constantes utilizadas em todo o projeto.

Este módulo centraliza valores fixos que podem ser reutilizados
por diferentes componentes da aplicação.

Manter essas informações em um único local facilita a manutenção
e evita a repetição de valores ao longo do código.
"""

# Tempo máximo (em segundos) para aguardar uma resposta HTTP.
DEFAULT_TIMEOUT: int = 10

# Cabeçalho HTTP utilizado para identificar a aplicação durante
# as requisições aos sites.
DEFAULT_USER_AGENT: str = (
    "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/138.0.0.0 "
    "Safari/537.36"
)

# Cabeçalhos HTTP padrão enviados em todas as requisições.
DEFAULT_HEADERS: dict[str, str] = {
    "User-Agent": DEFAULT_USER_AGENT
}