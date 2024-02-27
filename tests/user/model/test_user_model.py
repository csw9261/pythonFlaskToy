from tests.factory.test_factory import db

class User(db.Model):
    __tablename__ = 'user' # 테이블 이름 선언 
    __table_args__ = {'extend_existing': True} # 테스트 환경에서 같은 모듈을 여러번 import 하면 중복적으로 선언될 수 있는데 그걸 가능하게하려고 추가
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(255))

# 출력 형식 설정 
# ex) <User id=1, username=john_doe, email=john@example.com>
def __repr__(self):
    return '<User id={}, username={}, email={}>'.format(self.id, self.username, self.email)

