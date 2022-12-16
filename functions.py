import json


class PostsHandler:
    def __init__(self, path):
        self.path = path

    def load_post_from_json(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def search_post(self, sub_string):
        posts = []

        for line in self.load_post_from_json():
            if sub_string.lower() in line["content"].lower():
                posts.append(line)
                print(posts)

        return posts

    def add_post(self, post):
        posts = self.load_post_from_json()
        posts.append(post)
        return self.save_post_to_json(posts)

    def save_post_to_json(self, posts):
        try:
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(posts, file)
        except Exception as e:
            return e


def save_upload_picture(picture):
    filename = picture.filename
    filetype = filename.split('.')[-1]

    if filetype not in ['jpeg', 'jpg', 'bmp', 'svg']:
        return

    picture.save(f'./uploads/{filename}')

    return f'uploads/{filename}'
