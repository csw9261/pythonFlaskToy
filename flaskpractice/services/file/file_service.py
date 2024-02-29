from flask import jsonify
from werkzeug.datastructures import FileStorage

import os

class FileService():
    def readingFile(file: FileStorage):
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
    
        else:
            filename = file.filename
            filepath_and_name = os.path.join('./static/files', filename)
            file.save(filepath_and_name)
            
            with open(filepath_and_name, 'r', encoding='utf-8') as file:
                file_contents = file.read()
            
            os.remove(filepath_and_name) # 읽기 완료 후 저장한 파일 삭제 
            
            return file_contents

            