from flask import render_template, Blueprint, request
from functions import load_post, search_post

main_blueprint = Blueprint("mainbluerint", __name__)

@main_blueprint.route('/')
def main_page():
    return render_template("index.html")

@main_blueprint.route('/search')
def search_page():
    key = request.args.get('s', '')
    posts = load_post()
    found_posts = search_post(key, posts)
    return render_template('post_list.html', posts=found_posts, key = key)