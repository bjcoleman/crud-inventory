
from flask import Flask
import json

from product_inventory import ProductInventory

pi = ProductInventory({})

app = Flask(__name__)


@app.route('/')
def current_inventory():
    return json.dumps({})


if __name__ == '__main__':
    app.run(debug=True)
