from flask import Flask, render_template

from uploadfile.controller import fileuploadcontroller
from main.controller import maincontroller
from user.controller import usercontroller

from factory import create_app

from config.config import DB_Config

app = create_app()

# Docker 컨테이너 내에서 Flask 애플리케이션을 Gunicorn과 함께 실행하려고 할 때, 
# app.run()도 동시에 실행되려고 하면서 포트 충돌이 발생하기 때문에 해당 조건을 넣어야 한다.
if __name__ == '__main__':
    app.run(debug=True)

