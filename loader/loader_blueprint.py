from flask import Blueprint, render_template, request, current_app
from functions import save_upload_picture, PostsHandler
import logging

load_photo_blueprint = Blueprint('load_photo_blueprint', __name__, template_folder='..templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@load_photo_blueprint.route('/post')
def add_new_post():
    """
    Форма отправки нового посто
    """
    return render_template('post_form.html')


@load_photo_blueprint.route('/post', methods=['POST'])
def add_new_post_from_user():
    """
    Проверка и загрузка поста пользователя. Если отправлена не картинка из позволенного списка или картинка не была
    передана - возвращает ошибку.
    """
    picture = request.files.get('picture')
    content = request.form.get('content')

    # Проверка наличия картинки и текста, если нет одного или другого выдает ошибку
    if not picture or not content:
        return 'Данные не получены'

    picture_path = save_upload_picture(picture)

    # Если файл имеет неподходящий формат, выдает ошибку
    if not picture_path:
        logging.info(f'Файл: {picture.filename} - не изображение')
        return 'Файл - не изображение'

    # Подтягиваем класс загрузки и отображения постов
    posts_handler = PostsHandler(current_app.config['POST_PATH'])
    new_post = {'pic': picture_path, 'content': content}

    # Ловим редкую ошибку загрузки поста, передаем данные в лог
    error = posts_handler.add_post(new_post)
    if error:
        logging.error(f"Ошибка загрузки поста {error}")
        return 'Ошибка загрузки'

    return render_template('post_uploaded.html', picture_path=picture_path, content=content)
