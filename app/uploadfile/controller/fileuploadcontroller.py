from flask import Flask, request
from flask import Blueprint, jsonify
import logging
from uploadfile.model.fileuploadmodel import fileuploadmodelClass


# 블루 프린트 생성
upload_blueprint = Blueprint('upload_blueprint', __name__, url_prefix='/')

class fileUpLoadControllerClass:

    @upload_blueprint.route('/uploadfile', methods=['POST'])
    def uploadfile():
        file = request.files.get('uploadFile')

        result = fileuploadmodelClass.uploadfile(file)

        return result  
    
    @upload_blueprint.route('/getFileContents', methods=['GET'])
    def getFileContents():
        file_name = request.args.get('file_name')

        result, status_code = fileuploadmodelClass.getFileContents(file_name)

        return jsonify(result), status_code