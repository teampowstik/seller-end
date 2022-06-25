from flask import render_template, Blueprint

general = Blueprint('general', __name__)

@general.route("/", methods=['GET', 'POST'])
@general.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('general/home.html', title="Powstik-Seller-Portal")

@general.app_errorhandler(Exception)
def errorHandler(Exception):
    return render_template ("general/error.html", title="Error")