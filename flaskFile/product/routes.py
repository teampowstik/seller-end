from flask import flash, render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from flaskFile.models import Product as PD
from flaskFile import db
from flaskFile.product.forms import Product
from flaskFile import utils

product = Blueprint('product', __name__)

@product.route("/upload-product", methods=['GET', 'POST'])
@login_required
def uploadProduct():
    form = Product()
    if form.validate_on_submit():
        try: 
            image_1_url = utils.get_image_url(utils.save_image(form.image_1.data))
            image_2_url = utils.get_image_url(utils.save_image(form.image_2.data))
            image_3_url = utils.get_image_url(utils.save_image(form.image_3.data))
            image_4_url = utils.get_image_url(utils.save_image(form.image_4.data))

            product = PD(name=form.name.data,\
                description=form.description.data,\
                    userId=current_user.id,\
                        sku_code=form.sku_code.data,\
                            mrp=form.mrp.data,\
                                selling_price=form.selling_price.data,\
                                    shipping_cost=form.shipping_cost.data,\
                                        bulk_pricing=form.bulk_pricing.data,\
                                            image_1 = image_1_url,\
                                                image_2 = image_2_url,\
                                                    image_3 = image_3_url,\
                                                        image_4 = image_4_url
                )
            db.session.add(product)
            db.session.commit()
            flash("Thank you for uplaod")
            return redirect(url_for('general.home'))
        except:
            return redirect(url_for('general.errorHandler'))
    return render_template('product/upload-product.html', title='Find-Product', form=form)


