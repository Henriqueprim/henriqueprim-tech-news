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

    try:
        if user_input == "0":
            print("Digite quantas notícias serão buscadas:")
            amount = int(input())
            print(get_tech_news(amount))
        elif user_input == "1":
            print("Digite o título:")
            title = input()
            print(search_by_title(title))
        elif user_input == "2":
            print("Digite a data no formato aaaa-mm-dd:")
            date = input()
            print(search_by_date(date))
        elif user_input == "3":
            print("Digite a categoria:")
            category = input()
            print(search_by_category(category))
        elif user_input == "4":
            print(top_5_categories())
        elif user_input == "5":
            print("Encerrando script\n")
        else:
            sys.stderr.write("Opção inválida\n")
    except ValueError as e:
        sys.stderr.write(str(e))
