import json, os
from app import app

def loadCategories():
    with open("%s/data/categories.json" % app.root_path) as f:
        return json.load(f)

def loadProducts(category_id=None):
    with open("%s/data/products.json" % app.root_path) as f:
        products = json.load(f)

        if category_id:
            products = [p for p in products if p['category_id'] == int(category_id)]
        return products