from main import database


class User_auth(database.Model):
    auth_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(
        database.Integer, ForeignKey("user.user_id"), nullable=False
    )
    access_token = database.Column(database.String(255), nullable=False)
    refresh_token = database.Column(database.String(255), nullable=False)
    phone_number_verification = database.Column(database.Integer, nullable=False)
    email_verification_token = database.Column(database.String(255), nullable=False)
    hashed_password = database.Column(database.String(255), nullable=False)
    username = database.Column(database.String(255), nullable=False)
    last_logged_in = database.Column(database.TIMESTAMP)
    email_verified = database.Column(database.Boolean, nullable=False)
    phone_number_verified = database.Column(database.Boolean, nullable=False)
    password_reset_token = database.Column(database.String(255), nullable=False)
    locked_until = database.Column(database.Timestamp)
    two_factor_enabled = database.Column(database.Boolean, nullable=False)
    device_id = database.Column(database.Integer, nullable=False)
    ip_address = database.Column(database.String(255), nullable=False)
    user_agent = database.Column(database.String(255), nullable=False)
