import os, json, logging
from flask import jsonify

class fileuploadmodelClass:

    @staticmethod
    def uploadfile(file):
        if not file:
            logging.error('###error: ' 'No file part')
            return jsonify({'error': 'No file part'}), 400

        if file.filename == '':
            logging.error('###error' ' No selected file')
            return jsonify({'error': 'No selected file'}), 400
        
        file.save('./static/files/' + file.filename)
        return jsonify({
                        'message': 'File successfully uploaded'
                    }), 200  
        
    @staticmethod
    def getFileContents(file_name):
        logging.error("###file_name-> " + file_name)

        #파일 상대 경로 
        relative_path = os.path.join('static', 'files', file_name)
        logging.error("###relative_path-> " + relative_path)

        #파일 전체 경로
        file_path = os.path.join(os.getcwd(), relative_path)
        logging.error("###file_path-> " + file_path)

        # 파일이 존재하는지 확인
        if not os.path.exists(file_path):
            return {"error": "File not found"}, 404
        
        # 파일이 JSON 형식인지 확인 후 return 
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data, 200
        
        except (ValueError, json.JSONDecodeError):
            return {"error": "Invalid JSON format"}, 400        