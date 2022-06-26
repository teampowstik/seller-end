from flask import flash, render_template, redirect, url_for, Blueprint

admin = Blueprint('admin', __name__)

@admin.route("/", methods=['GET', 'POST'])
@admin.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('admin/home.html', title="Powstik-Seller-Portal")

# @admin.get("/product/<int:id>")
# def product_by_id(id):



