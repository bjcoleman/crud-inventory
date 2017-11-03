
from flask import Flask, request
import json

from product_inventory import ProductInventory

pi = ProductInventory({})

app = Flask(__name__)


@app.route('/')
def current_inventory():
    return json.dumps({})


@app.route('/search')
def inventory_search():
    query = request.args.get('query', '')
    results = []
    for product in pi.get_product_list():
        if product.startswith(query):
            quantity = pi.get_quantity(product)
            results.append({'name': product, 'quantity': quantity})
    return json.dumps(results)


    return '[]'


if __name__ == '__main__':
    app.run(debug=True)
