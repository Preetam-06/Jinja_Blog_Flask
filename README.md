# Jinja Flask Learning

A small Flask blog application built to practice Flask routing, Jinja templating, static CSS, and rendering data from an external JSON API.

The app fetches blog posts from an npoint API endpoint, converts each JSON item into a `Post` object, and displays the posts through Jinja templates.

## Features

- Flask web server with two routes
- Home page that lists all blog posts
- Dynamic post detail pages using URL parameters
- Jinja template rendering with looped post data
- Simple `Post` model class for blog data
- External JSON API data source
- Custom styling from `static/css/styles.css`

## Project Structure

```text
Jinja-Flask-learning/
|-- main.py
|-- post.py
|-- templates/
|   |-- index.html
|   `-- post.html
|-- static/
|   `-- css/
|       `-- styles.css
|-- .gitignore
`-- README.md
```

## How It Works

### `main.py`

`main.py` is the main Flask application file.

It:

- Creates the Flask app instance
- Fetches post data from:

```text
https://api.npoint.io/c790b4d5cab58020d391
```

- Converts API data into `Post` objects
- Renders the home page with all posts
- Renders individual post pages based on post ID

Available routes:

| Route | Description |
| --- | --- |
| `/` | Shows all blog posts |
| `/post/<int:num>` | Shows one blog post by ID |

### `post.py`

Contains the `Post` class used to store each blog post's:

- `id`
- `title`
- `subtitle`
- `body`

### `templates/index.html`

Displays the blog homepage. It loops through the `posts` list and creates a card for each post.

### `templates/post.html`

Displays a single blog post with its title, subtitle, and body.

### `static/css/styles.css`

Contains the page layout, card styling, header styling, typography, and fixed footer.

## Requirements

- Python 3
- Flask
- Requests

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Jinja-Flask-learning.git
cd Jinja-Flask-learning
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install flask requests
```

## Running the App

Start the Flask app:

```bash
python main.py
```

Then open:

```text
http://127.0.0.1:5000/
```

To view a single post, open a URL like:

```text
http://127.0.0.1:5000/post/1
```

## Example Flow

1. User visits `/`.
2. Flask calls `get_posts()`.
3. `get_posts()` requests JSON data from the API.
4. Each JSON object is converted into a `Post` object.
5. `index.html` displays all posts.
6. User clicks `Read`.
7. Flask loads `/post/<id>` and renders `post.html`.

## Notes

- The app depends on the external npoint API being available.
- Debug mode is enabled in `main.py`, which is useful for learning and development.
- Before deploying publicly, set `debug=False` or use environment-based configuration.

## Possible Improvements

- Add a `requirements.txt` file
- Improve the 404 behavior for missing posts
- Use `url_for()` for the CSS file path
- Add error handling for failed API requests
- Cache API responses to avoid fetching posts on every page load

## License

This project is for learning purposes. You can add a license file if you plan to publish or reuse it.
