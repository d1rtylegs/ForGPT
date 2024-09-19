from flask import render_template, Blueprint, request
from functions import save_post

loader_blueprint = Blueprint("loader_blueprint", __name__)


@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    if request.method == "POST":
        picture = request.files.get('picture')
        content = request.form.get('content')

        if picture:  # Проверка на наличие файла
            filename = picture.filename
            picture.save(f"./uploads/images/{filename}")
            save_post(filename, content)
            return render_template('post_uploaded.html', picture=f"./uploads/images/{filename}", content=content)
        else:
            return "Ошибка загрузки: файл не был выбран", 400  # Ответ с ошибкой, если файл не выбран

    return render_template('post_form.html', picture=None, content="")