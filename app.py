app.py

from flask import Flask, render_template, request, redirect, url_for
from models import db, Farmer, Product

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crop2cart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/farmer/<int:id>')
def farmer(id):
    farmer = Farmer.query.get_or_404(id)
    return render_template('farmer.html', farmer=farmer)

@app.route('/add_product', methods=['POST'])
def add_product():
    product_name = request.form['name']
    product_price = request.form['price']
    farmer_id = request.form['farmer_id']
    new_product = Product(name=product_name, price=product_price, farmer_id=farmer_id)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(debug=True)
