from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if username and password:
            return redirect(url_for('home'))

        error = 'Please enter username and password.'

    return render_template('login.html', error=error)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/how')
def how():
    return render_template('how.html')


@app.route('/assessment', methods=['GET', 'POST'])
def assessment():
    return render_template('assessment.html')


@app.route('/idea', methods=['GET', 'POST'])
def idea():
    return render_template('idea.html')


@app.route('/features')
def features():
    return render_template('features.html')


@app.route('/future')
def future():
    return render_template('future.html')


if __name__ == '__main__':
    app.run(debug=True)
