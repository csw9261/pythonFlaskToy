from flask import Blueprint, request, jsonify

from services.user.user_service import UserService

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix="/user")

class UserController:
    @user_blueprint.route('/insertUser', methods=['POST'])
    def isnertUser():
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # user table insert 
        success, message = UserService.insert_user(username, email, password)
        if not success:
            return jsonify({'error': message}), 500  # 서버 내부 오류 응답
        
        return jsonify({'message': message}), 200
    
    @user_blueprint.route('/findUser', methods=['GET'])
    def selectUser():
        # 'username' 파라미터가 없을 경우 None을 반환
        username = request.args.get('username')
        
        success, result  = UserService.select_user(username)
        
        if not success:
            return jsonify({'error': result}), 500  # 서버 내부 오류 응답 
        return result    
    
    @user_blueprint.route('/permission_check', methods=['GET'])
    def permission_check():
        request_email = request.args.get('email')
        request_userpassword = request.args.get('password')
        
        permission_check_result =  UserService.permission_check(request_email, request_userpassword)

        if permission_check_result:
            return jsonify({'message': 'Success'})
        else:
            return jsonify({'message' : 'Fail'})
        
        
        
        