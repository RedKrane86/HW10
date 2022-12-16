from flask import Blueprint, render_template, request, current_app
from functions import PostsHandler
import logging


main_page_blueprint = Blueprint('main_page_blueprint', __name__, template_folder='..templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@main_page_blueprint.route('/')
def index_page():
    return render_template('index.html')


@main_page_blueprint.route('/search')
def search_page():
    result = request.args.get('s', '')
    logging.info(f'Поиск: {result}')
    posts_handler = PostsHandler(current_app.config['POST_PATH'])
    posts = posts_handler.search_post(result)

    return render_template('post_list.html', posts=posts, result=result)

