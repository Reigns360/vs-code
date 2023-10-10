from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample in-memory data structures
books = [
    {"id": 1, "title": "Book 1", "price": 10.99},
    {"id": 2, "title": "Book 2", "price": 12.99},
    # Add more books as needed
]

users = {"user": "password"}  # Sample user data


@app.route('/')
def index():
    return render_template('index.html', books=books)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if users.get(username) == password:
        session['username'] = username
        return redirect('/')
    else:
        return "Invalid credentials"


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        # Handle adding items to the cart
        pass

    return render_template('cart.html')


@app.route('/order', methods=['POST'])
def order():
    if 'username' not in session:
        return redirect('/login')

    # Handle order processing logic
    pass


if __name__ == '__main__':
    app.run(debug=True)



