
from flask import Flask, request, Response
import json

from product_inventory import ProductInventory

pi = ProductInventory({})

app = Flask(__name__)


@app.route('/')
def current_inventory():
    return json.dumps({})


@app.route('/search')
def inventory_search():
    if len(request.args) != 1:
        message = "Search requires a single query parameter named query"
        return Response('["msg": "{}"]'.format(message), status=400)

    query = request.args.get('query', '')
    results = []
    for product in pi.get_product_list():
        if product.startswith(query):
            quantity = pi.get_quantity(product)
            results.append({'name': product, 'quantity': quantity})
    return json.dumps(results)


if __name__ == '__main__':
    app.run(debug=True)
