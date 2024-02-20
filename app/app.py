from flask import Flask

from uploadfile.controller import fileuploadcontroller
from main.controller import maincontroller

app = Flask(__name__)

# blueprint 등록
app.register_blueprint(maincontroller.main_blueprint)
app.register_blueprint(fileuploadcontroller.upload_blueprint)
    
app.run(debug=True)
#app.run()
