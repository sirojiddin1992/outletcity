from models import db  # `db` ni `models/__init__.py` faylidan import qilamiz

class Discount(db.Model):
    __tablename__ = 'discounts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'), nullable=False)

    shop = db.relationship('Shop', back_populates='discounts')
