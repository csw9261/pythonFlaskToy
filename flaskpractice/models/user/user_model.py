from db_init import db

class User_Table(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(255))

# 출력 형식 설정 
# ex) <User id=1, username=john_doe, email=john@example.com>
def __repr__(self):
    return '<User id={}, username={}, email={}>'.format(self.id, self.username, self.email)