from flask import Flask, send_from_directory
from main.main_blueprint import main_page_blueprint
from loader.loader_blueprint import load_photo_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_page_blueprint)
app.register_blueprint(load_photo_blueprint)

app.config['POST_PATH'] = POST_PATH


@app.route("/uploads/<path:path>")
def static_dir(path):
    """
    Показывает пользователю пост загруженый другими пользователями
    """
    return send_from_directory("uploads", path)


app.run(debug=True)
