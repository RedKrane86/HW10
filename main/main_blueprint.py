from flask import Blueprint, render_template, request, current_app
from functions import PostsHandler
import logging

main_page_blueprint = Blueprint('main_page_blueprint', __name__, template_folder='..templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@main_page_blueprint.route('/')
def index_page():
    """
    Главная страничка
    """
    return render_template('index.html')


@main_page_blueprint.route('/search')
def search_page():
    """
    Страничка поиска
    """
    result = request.args.get('s', '')

    # Записывает слово поиска в лог
    logging.info(f'Поиск: {result}')

    # Подтягивает класс загрузки и отображения постов
    posts_handler = PostsHandler(current_app.config['POST_PATH'])
    posts = posts_handler.search_post(result)

    return render_template('post_list.html', posts=posts, result=result)
