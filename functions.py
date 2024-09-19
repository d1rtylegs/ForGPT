import json

def save_post(filename, content):
    post = {
        "pic": f"/uploads/images/{filename}",
        "content": content
    }
    try:
        with open('posts.json', 'r', encoding='utf-8') as file:
            posts = json.load(file)
    except FileNotFoundError:
        posts = []
    posts.append(post)

    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)

def load_post(file_name='posts.json'):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        return 'Error'

def search_post(key, posts):
    key = key.lower()
    result = []
    for post in posts:
        if key in post['content'].lower():
            result.append({
                'pic': post['pic'],
                'content': post['content']
            })
    return result


