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
    
app.run(debug=True)
#app.run()
