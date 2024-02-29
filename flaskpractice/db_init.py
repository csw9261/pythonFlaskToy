from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

# db 초기화 
def init_app_with_db(app):
    db.init_app(app)
    Migrate(app, db)
