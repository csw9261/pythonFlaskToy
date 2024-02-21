from flask import Flask, render_template

from uploadfile.controller import fileuploadcontroller
from main.controller import maincontroller

app = Flask(__name__)

# error handler 등록 
@app.errorhandler(404)
def page_not_found(error):
    return render_template('/error/404_error.html'), 404

@app.errorhandler(500)
def page_server_error(error):
    return render_template('/error/500_error.html'), 500

# blueprint 등록
app.register_blueprint(maincontroller.main_blueprint)
app.register_blueprint(fileuploadcontroller.upload_blueprint)
    
# Docker 컨테이너 내에서 Flask 애플리케이션을 Gunicorn과 함께 실행하려고 할 때, 
# app.run()도 동시에 실행되려고 하면서 포트 충돌이 발생하기 때문에 해당 조건을 넣어야 한다.
if __name__ == '__main__':
    app.run(debug=True)

