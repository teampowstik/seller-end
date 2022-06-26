from flask import  Blueprint, jsonify
from flaskFile import db, bcrypt
import flaskFile
from flaskFile.models import User as US
from flaskFile.models import Product as PD
import secrets

admin = Blueprint('admin', __name__)

@admin.get("/add-user/<int:key>/<string:email>/<string:pswd>")
def add_seller(key: int, email: str, pswd: str):
    if key != flaskFile.config.KEY:
        try:
            ps_id = secrets.token_hex(4)
            hashed_password = bcrypt.generate_password_hash(pswd).decode('utf-8')
            user = US(email = email, password = hashed_password, ps_id = ps_id)
            db.session.add(user)
            db.session.commit()
            return ps_id
        except:
            return "Data Error"
    return "ERROR"


@admin.get("/get-products/<int:key>/<string:ps_id>")
def get_product_by_user(key: int, ps_id: str):
    if key != flaskFile.config.KEY:
        products = PD.query.filter(PD.userId == ps_id).all()
        result = []
        for product in products:
            details = {
                "id": product.id,
                "name": product.name,
                "sku_code": product.sku_code,
                "description": product.description,
                "mrp": product.mrp,
                "selling_price": product.selling_price,
                "shipping_cost": product.shipping_cost,
                "bulk_pricing": product.bulk_pricing,
                "userId": product.userId,
                "image_1": product.image_1,
                "image_2": product.image_2,
                "image_3": product.image_3,
                "image_4": product.image_4,
            }
            result.append(details)
        return jsonify(result)
    return "ERROR"