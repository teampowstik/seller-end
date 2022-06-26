from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class Product(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    sku_code = IntegerField('SKU Code', validators=[DataRequired()])
    mrp = IntegerField('MRP', validators=[DataRequired()])
    selling_price = IntegerField('Selling Price', validators=[DataRequired()])
    shipping_cost = IntegerField('Shipping Cost', validators=[DataRequired()])
    bulk_pricing = IntegerField('Bulk Pricing', validators=[DataRequired()])
    image_1 = FileField("Product picture 1", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    image_2 = FileField("Product picture 2", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    image_3 = FileField("Product picture 3", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    image_4 = FileField("Product picture 4", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    submit = SubmitField('Upload Prouct')