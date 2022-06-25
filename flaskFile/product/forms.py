from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class Product(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    sku_code = IntegerField('SKU Code', validators=[DataRequired()])
    mrp = IntegerField('MRP', validators=[DataRequired()])
    selling_price = IntegerField('Selling Price', validators=[DataRequired()])
    shipping_cost = IntegerField('Shipping Cost', validators=[DataRequired()])
    bulk_pricing = IntegerField('Bulk Pricing', validators=[DataRequired()])

    submit = SubmitField('Upload Prouct')