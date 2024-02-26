from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config.config import DB_Config

# 각 컨트롤러 모듈 임포트
from uploadfile.controller import fileuploadcontroller
from main.controller import maincontroller
from user.controller import usercontroller

# SQLAlchemy 및 Flask-Migrate 인스턴스 생성
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # DB 설정 적용
    app.config.from_object(DB_Config)
    
    # SQLAlchemy 및 Flask-Migrate 초기화
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 에러 핸들러 설정
    addErrorHandler(app)
    
    # 블루프린트 등록
    registerBlueprint(app)

    return app

def addErrorHandler(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('/error/404_error.html'), 404

    @app.errorhandler(500)
    def page_server_error(error):
        return render_template('/error/500_error.html'), 500    

def registerBlueprint(app):
    app.register_blueprint(maincontroller.main_blueprint)
    app.register_blueprint(fileuploadcontroller.upload_blueprint)
    app.register_blueprint(usercontroller.user_blueprint)
