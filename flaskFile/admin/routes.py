from flask import  Blueprint
from flaskFile import db, bcrypt
import flaskFile
from flaskFile.models import User as US
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


