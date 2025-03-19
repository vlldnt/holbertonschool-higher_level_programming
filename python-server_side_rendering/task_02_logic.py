from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', "r") as file:
        item = json.load(file)
        items_list = item.get('items', [])
    return render_template('items.html', items=items_list)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        with open('products.json', "r", encoding='utf-8') as file:
            product = json.load(file)
            return product
    
    elif source == 'csv':
        data = []
        with open ("products.csv", 'r', encoding='utf-8') as file:
            product = csv.DictReader(file)
            for row in product:
                row['id'] = int(row.get('id', 0))
                row['name'] = row.get('name', 'N/A')
                row['category'] = row.get('category', 'N/A')
                row['price'] = float(row.get('price', 0.0))
                data.append(row)
            return data
    else:
        return render_template('products_display.html', error="Wrong source")
    
    if product_id:
        products = [product for product in data if product['id'] == product_id]
        if not product_id:
            return render_template('products_display.html', error="Product not found")
    else:
        return render_template('products_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
