from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)


url= "https://api.npoint.io/c790b4d5cab58020d391"

def get_posts():
    response = requests.get(url)
    data = response.json()
    posts_list = []
    for post in data:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        posts_list.append(post_obj)
    return posts_list

@app.route('/post/<int:num>')
def post_page(num):
    posts = get_posts()
    for post in posts:
        if post.id == num:
            re_post = post
            return render_template("post.html", post=re_post)
        else:
            return "Post not found", 404

@app.route('/')
def home():
    return render_template("index.html", posts=get_posts())

if __name__ == "__main__":
    app.run(debug=True)
