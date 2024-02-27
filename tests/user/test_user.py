from tests.factory.test_factory import db
from tests.user.model.test_user_model import User
from tests.test_app import client

from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError


def test_insert_user(client):
    assert insert_user('testuser', 'test@example.com', 'password')[0] == True
    user = User.query.first()
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
        
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

def test_select_user(client):
    insert_user('testuser', 'test@example.com', 'password')
    assert select_user('testuser')[0] == True

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
    