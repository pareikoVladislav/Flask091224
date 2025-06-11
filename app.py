from flask import Flask
app = Flask(__name__)

@app.route('/home')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/info')  # http://127.0.0.1:5000/info
def get_project_info():
    return "<h1>THIS IS A PROJECT INFO</h1>"


@app.route('/user/<uuid:id>')
def get_user_by_uuid(id):
    return f"User with uuid: {id}"


@app.route('/user/<string:username>')
def get_user_name(username: str):
    return f"Current user with username: {username}"


@app.route('/user/<string:username>/posts/<int:post_id>')
def get_user_post_by_id(username, post_id):
    return f"Post from user: {username} with ID {post_id}"


@app.route('/files/<path:filepath>')
def get_file_by_path(filepath):
    return f"File: {filepath}"


# path/to/my/file

if __name__ == '__main__':
    app.run(debug=True)
# 127.0.0.1 -> -> localhost
# 0.0.0.0
