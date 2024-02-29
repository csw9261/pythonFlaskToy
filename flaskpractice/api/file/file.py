from flask import Blueprint, request

from services.file.file_service import FileService

file_blueprint = Blueprint('file_blueprint', __name__, url_prefix="/file")

class FileController():
    @file_blueprint.route('/upload', methods=['POST'])
    def uploadFile():
        
        file = request.files.get('uploadFile')
        if file:
            result = FileService.readingFile(file)
            
            return result
        