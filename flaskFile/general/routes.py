from flask import flash, render_template, redirect, url_for, Blueprint

general = Blueprint('general', __name__)

@general.route("/", methods=['GET', 'POST'])
@general.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('general/home.html', title="Powstik-Seller-Portal")


@general.app_errorhandler(413)
def page_not_found(Exception):
    flash("Image file must be less than 500kb", "error")
    return redirect(url_for('product.uploadProduct'))


@general.app_errorhandler(Exception)
def errorHandler(Exception):
    return render_template ("general/error.html", title="Error")

