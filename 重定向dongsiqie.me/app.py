from flask import Flask, redirect, abort, request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://dongsiqie.me', code=302)

@app.route('/<path:path>', methods=['GET', 'POST'])
def redirect_all(path):
    if 'create' in path or 'fd' in path or 'web' in path:
        return redirect('http://127.0.0.1', code=301)
    if request.method == 'POST':
        return redirect('http://127.0.0.1', code=301)
    return redirect('https://dongsiqie.me', code=302)

if __name__ == '__main__':
    app.run()