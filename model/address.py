from main import database

class Address(database.Model)  
    address_id = database.Column(database.Integer,primary_Key=True,nullable=False)
    user_id = database.Column(database.Integer,ForeignKey("user.user_id"),nullable=False)
    address_line1 = database.Column(database.String(255),nullable=False)
    city = database.Column(database.String(255),nullable=False)
    state = database.Column(database.String(255),nullable=False)
    country = database.Column(database.String(255),nullable=False)
    postal_code = database.Column(database.String(255),nullable=False)
    is_default = database.Column(database.Boolean)


