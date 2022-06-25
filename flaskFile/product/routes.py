from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from flaskFile.models import Product as PD
from flaskFile import db
from flaskFile.product.forms import Product

product = Blueprint('product', __name__)

@product.route("/upload-product", methods=['GET', 'POST'])
@login_required
def uploadProduct():
    form = Product()
    if form.validate_on_submit():
        try: 
            product = PD(name=form.name.data,\
                description=form.description.data,\
                    userId=current_user.id,\
                        sku_code=form.sku_code.data,\
                            mrp=form.mrp.data,\
                                selling_price=form.selling_price.data,\
                                    shipping_cost=form.shipping_cost.data,\
                                        bulk_pricing=form.bulk_pricing.data\
                )
            db.session.add(product)
            db.session.commit()
        except:
            return redirect(url_for('general.errorHandler'))
    return render_template('product/upload-product.html', title='Find-Product', form=form)


