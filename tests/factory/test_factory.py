from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from tests.config.test_config import test_DB_Config

# SQLAlchemy 및 Flask-Migrate 인스턴스 생성
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(test_DB_Config)
    app.config['SQLALCHEMY_ECHO'] = True # SQLAlchemy가 실행하는 모든 SQL 쿼리를 출력
    db.init_app(app)
    
    return app


