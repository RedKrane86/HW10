import json


# Класс отправки и отображения постов
class PostsHandler:
    def __init__(self, path):
        self.path = path

    def load_post_from_json(self):
        """
        Распаовывет данные из файла JSON
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def search_post(self, sub_string):
        """
        Проводит поиск постов по вхожденю указанного слова, возвражает все посты с этим словом
        """
        posts = []
        for line in self.load_post_from_json():
            if sub_string.lower() in line["content"].lower():
                posts.append(line)
                print(posts)
        return posts

    def save_post_to_json(self, posts):
        """
        Сохраняет новый пост в JSON файл, ловит редкую ошибку загрузки
        """
        try:
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(posts, file)
        except Exception as e:
            return e

    def add_post(self, post):
        """
        Добавляет новый пост в JSON файл
        """
        posts = self.load_post_from_json()
        posts.append(post)

        return self.save_post_to_json(posts)


def save_upload_picture(picture):
    """
    Проверяет и сохраняет изображение в uploads
    """
    filename = picture.filename
    filetype = filename.split('.')[-1]

    # Проверяет доступные форматы изображений
    if filetype not in ['jpeg', 'jpg', 'bmp', 'svg', 'png', 'jp2']:
        return

    picture.save(f'./uploads/{filename}')

    return f'uploads/{filename}'
