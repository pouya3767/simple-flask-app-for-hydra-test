from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    is_login = False
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'p0uya3767' and password == '123':
            is_login = True
    return render_template('index.html', is_login=is_login)


if __name__ == '__main__':
    app.run()

