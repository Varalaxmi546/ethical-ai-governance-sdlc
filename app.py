@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # Allow any non-empty username and password
        if username and password:
            return redirect(url_for('home'))

        error = 'Please enter username and password.'

    return render_template('login.html', error=error)
