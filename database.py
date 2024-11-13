# (url) host + port
# host = 127.0.0.1
# port = 5432
# user = postgres
# database = ecommerce
# password = self.password

# SQLALCHEMY_DATABASE_URI = "postgresql+psychog2://{user}:{password}@

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

database = SQLAlchemy()
migrate = Migrate()
