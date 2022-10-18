from flask import render_template, request
from app import dao
from app import app


@app.route("/")
def index():
    categories = dao.loadCategories()

    cate_id = request.args.get('category_id')
    products = dao.loadProducts(category_id=cate_id)
    print(categories)
    return render_template("index.html",
                           categories=categories,
                           products=products)


if __name__ == "__main__":
    app.run(debug=True)