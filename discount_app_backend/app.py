from flask import Flask, render_template, request, redirect, url_for
from models import db  # Bu yerda db obyektini import qilamiz
from models.discount import Discount
from models.shop import Shop
from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discounts.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)  # `db` obyektini `app` bilan bog'lash

@app.route('/')
def home():
    shops = Shop.query.all()
    return render_template('home.html', shops=shops)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Login logic
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Register logic
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/add-discount', methods=['GET', 'POST'])
def add_discount():
    if request.method == 'POST':
        # Add discount logic
        return redirect(url_for('home'))
    return render_template('add_discount.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Baza jadvalarini yaratish
    app.run(debug=True)
