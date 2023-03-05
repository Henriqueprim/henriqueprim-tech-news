from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title
)
from tech_news.scraper import get_tech_news
import sys


# Requisitos 11 e 12
def analyzer_menu():
    user_input = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.\n"
    )

    options = {
        '0': get_news,
        '1': get_by_title,
        '2': get_by_date,
        '3': get_by_category,
        '4': get_top_five,
        '5': exit_app
    }

    try:
        if user_input in options.keys():
            options[user_input]()
        else:
            sys.stderr.write("Opção inválida\n")
    except ValueError as e:
        sys.stderr.write(str(e))


def get_news():
    print("Digite quantas notícias serão buscadas:")
    amount = int(input())
    print(get_tech_news(amount))


def get_by_title():
    print("Digite o título:")
    title = input()
    print(search_by_title(title))


def get_by_date():
    print("Digite a data no formato aaaa-mm-dd:")
    date = input()
    print(search_by_date(date))


def get_by_category():
    print("Digite a categoria:")
    category = input()
    print(search_by_category(category))


def get_top_five():
    print(top_5_categories())


def exit_app():
    print("Encerrando script\n")
