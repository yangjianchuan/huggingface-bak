from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://dongsiqie.me', code=302)

@app.route('/<path:path>', methods=['GET', 'POST'])
def redirect_all(path):
    return redirect('https://dongsiqie.me', code=302)

if __name__ == '__main__':
    app.run()
