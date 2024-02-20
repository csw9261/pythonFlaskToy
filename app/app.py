import json
from flask import Flask, request
from main import index
from upload import fileupload

app = Flask(__name__)
app.register_blueprint(index.main) #main페이지 app.py와 연결
app.register_blueprint(fileupload.upload) #업로드 기능과 app.py와 연결

@app.route("/")
def test():
    return "test"

# Parameter 테스트
@app.route('/test/<testValue1><testValue2>')
def show_testValue(testValue1, testValue2):
    # show the user profile for that user
    return 'test %s %e' %testValue1 %testValue2

# Http Method 테스트 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "post"
    else:
        return "get"
    
app.run(debug=True)
#app.run()
