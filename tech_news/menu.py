import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_categories


def get_user_option():
    option_selected = input(
        "Selecione uma das opções a seguir:\n "
        "0 - Popular o banco com notícias;\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por categoria;\n "
        "4 - Listar top 5 categorias;\n "
        "5 - Sair."
    )

    return option_selected


def analyzer_menu():
    try:
        option_selected = get_user_option()

        options = {
            "0": lambda: get_tech_news(
                int(input("Digite quantas notícias serão buscadas:"))
            ),
            "1": lambda: search_by_title(input("Digite o título:")),
            "2": lambda: search_by_date(
                input("Digite a data no formato aaaa-mm-dd:")
            ),
            "3": lambda: search_by_category(input("Digite a categoria:")),
            "4": lambda: top_5_categories(),
            "5": lambda: print("Encerrando script"),
        }

        return options[option_selected]()

    except KeyError:
        print("Opção inválida", file=sys.stderr)
