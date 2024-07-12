from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# In-memory user database
users = []

# Admin credentials
admin_email = 'admin@gmail.com'
admin_password = 'admin@123'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    if email == admin_email and password == admin_password:
        session['logged_in'] = True
        flash('Welcome to Admin portal..!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Invalid credentials. Please try again.', 'danger')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/admin')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        users.append({'id': len(users) + 1, 'name': name, 'email': email})
        flash('User added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    user = next((u for u in users if u['id'] == user_id), None)
    if request.method == 'POST':
        user['name'] = request.form['name']
        user['email'] = request.form['email']
        flash('User updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_user.html', user=user)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    global users
    users = [u for u in users if u['id'] != user_id]
    flash('User deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

