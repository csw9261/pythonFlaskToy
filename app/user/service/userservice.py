from sqlalchemy.exc import SQLAlchemyError
from model.user_model import db, User
from werkzeug.security import generate_password_hash

import logging

def insert_user(username, email, password):
    try:
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256') # 비밀번호 해싱
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()  # 변경사항 커밋
    except SQLAlchemyError as e:
        db.session.rollback()  # 예외 발생 시 롤백
        return False, str(e)
    
    return True, "User successfully inserted"

def select_user(user_name):
    try:
        select_user_result = User.query.filter_by(username = user_name).first()
        
        if select_user_result:
            user_info_json = {
                'id': select_user_result.id,
                'username': select_user_result.username,
                'email': select_user_result.email
            }
        
        return True, user_info_json
    except SQLAlchemyError as e:
        return False, str(e)
        