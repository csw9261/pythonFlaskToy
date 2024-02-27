import pytest
import logging
from tests.factory.test_factory import create_app, db

# 전역 로깅 설정
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()
