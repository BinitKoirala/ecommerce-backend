from ..database import database


class User(database.Model):
    user_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    first_name = database.Column(database.String(255), nullable=False)
    last_name = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(255), nullable=False)
    gender = database.Column(database.String(255))
    phone_number = database.Column(database.String(255))
    address = database.Column(database.String(255))
    date_of_birth = database.Column(database.Date, nullable=False)
    profile_picture_url = database.Column(database.String(500))
    preferences = database.Column(database.JSON)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
