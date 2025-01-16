from flask import Flask, render_template, request, redirect, url_for, flash, session
from DB_Operations import fetch_all_items, insert_item, delete_item, fetch_item_by_id, update_item, validate_user, save_message, fetch_all_messages
from config import secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key()

@app.route('/')
def index2():
    items = fetch_all_items()
    return render_template('index.html',items=items)

@app.route('/admin')
def index():
    if 'username' not in session:
        return redirect(url_for('login')) 

    items = fetch_all_items() 
    messages = fetch_all_messages()
    return render_template('admin/index.html', items=items,messages=messages )


@app.route('/add_item', methods=["POST","GET"])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        insert_item(name,description)
        return redirect(url_for('index'))
    return render_template('admin/add.html')

@app.route('/edit/<id>', methods=["GET","POST"])
def edit_item(id):
    item = fetch_item_by_id(id)
    if not item:
        flash("Item Tidak Ditemukan")
        return redirect(url_for('index'))
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        update_item(id,name,description)
        return redirect(url_for('index'))
    return render_template('admin/edit.html',item=item)

@app.route('/delete/<id>', methods=["GET","POST"])
def delete_item_route(id):
    delete_item(id)
    return redirect(url_for('index'))

@app.route('/submit', methods=['POST'])
def submit_message():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        message = request.form['message']

        success = save_message(name, contact, message)
        
        if success:
            flash('Pesan berhasil dikirim!', 'success')
        else:
            flash('Gagal mengirim pesan. Coba lagi.', 'danger')
        
        return redirect(url_for('index2'))
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = validate_user(username, password)
        if user:
            session['username'] = username
            return redirect('/admin')  
        else:
            error = "Invalid username or password."

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None) 
    items = fetch_all_items()
    return render_template('index.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)