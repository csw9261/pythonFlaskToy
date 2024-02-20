from flask import request, Blueprint, jsonify
import os, json, logging

upload = Blueprint('upload', __name__, url_prefix='/')

@upload.route('/upload', methods=['POST'])
def uploadfile():
    if 'uploadFile' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['uploadFile']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    file.save('./static/files/' + file.filename)

    return jsonify({
                    'message': 'File successfully uploaded'
                   }), 200

@upload.route('/getFileContents', methods=['GET'])
def getFileContents():
    # 요청에서 파일 이름을 가져오기
    file_name = request.args.get('file_name')
    logging.error("file_name-> " + str(file_name))

    # 상대 경로 설정. Flask 앱 기준으로 파일 위치를 지정
    relative_path = os.path.join('static', 'files', file_name)
    logging.error("relative_path-> " + str(relative_path))

    # 파일의 전체 경로
    file_path = os.path.join(os.getcwd(), relative_path)
    logging.error("file_path-> " + str(file_path))

    
    # 파일이 존재하는지 확인
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
    
    # 파일이 JSON 형식인지 확인 후 return 
    try:
        with open(file_path, 'r', encoding='utf-8') as file: # with를 사용 시 빠져나오면서 자동으로 close 처리 시켜준다.
            data = json.load(file)
        return jsonify(data)
    
    except (ValueError, json.JSONDecodeError) as e:
        # 파일 내용이 유효한 JSON 형식이 아닐 경우
        return jsonify({"error": "Invalid JSON format"}), 400


