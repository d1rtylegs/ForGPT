from flask import Flask
from main.views import main_blueprint
from loader.views import loader_blueprint
from flask import send_from_directory


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

@app.route('/uploads/images/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('uploads/images', filename)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)



app.run()

