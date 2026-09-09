@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if username == 'admin' and password == 'admin123':
            return redirect(url_for('home'))

        error = 'Invalid username or password.'

    return render_template('login.html', error=error)
