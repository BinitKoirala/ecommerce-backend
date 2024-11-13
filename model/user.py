from ..database import database


class User(database.Model):
    user_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    username = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(255), nullable=False)
    gender = database.Column(database.String(255))
    phone_number = database.Column(database.String(255))
    address = database.Column(database.String(255))
    date_of_birth = database.Column(database.Date, nullable=False)
    profile_picture_url = database.Column(database.String(500))
    status = database.Column(
        database.Enum("active", "inactive", "banned", name="user_status_enum"),
        nullable=False,
    )
    role = database.Column(
        database.Enum("admin", "user", name="user_role_enum"), nullable=False
    )
    preferences = database.Column(database.JSON)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
