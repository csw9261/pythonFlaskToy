import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class DB_Config(object):
    
    # SQLAlchemy 및 Flask-Migrate 인스턴스 생성
    db = SQLAlchemy()
    migrate = Migrate()
    
    # SECRET_KEY -> Flask 및 여러 확장 기능에서 보안 관련 작업을 수행할 때 사용됩니다. 예를 들어, 세션, 쿠키, CSRF 보호 등에 사용
    # SECRET_KEY 설정 값을 환경 변수에서 불러오거나, 환경 변수가 설정되어 있지 않은 경우 기본값 'you-will-never-guess'를 사용하도록 하는 방식
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/pythonFlaskToy'
    
    # Flask-SQLAlchemy에 의해 SQLAlchemy의 이벤트 시스템을 사용하여 객체의 변경 사항을 추적하고, 자동으로 신호를 발생시키는 기능을 활성화할지 여부
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    