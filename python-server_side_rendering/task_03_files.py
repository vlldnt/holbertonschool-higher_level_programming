#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    with open('items.json') as json_file:
        data = json.load(json_file)
        items_list = data.get("items", [])

    return render_template('items.html', items=items_list)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    products = []

    if source == "json":
        with open('products.json', 'r') as file:
            products = json.load(file)
    elif source == "csv":
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                row['id'] = int(row.get('id', 0))
                row['category'] = row.get('category', 'N/A')
                row['name'] = row.get('name', 'N/A')
                row['price'] = float(row.get('price', 0.0))
                products.append(row)
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        products = [product for product in products if product.get("id") == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")
    return render_template('product_display.html', products=products)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)