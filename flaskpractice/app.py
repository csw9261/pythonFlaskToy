from flask import Flask
from flask_migrate import Migrate

from configs.db_config_local_local import LocalDBConfig
from configs.blue_print_config import BluePrintConfig
from db_init import init_app_with_db


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        
        # DB 설정 
        self.app.config.from_object(LocalDBConfig)
        init_app_with_db(self.app)
        
        #blueprint 설정
        BluePrintConfig.register_Blueprint(self.app)
    
# Flask CLI가 app를 못찾는 이유로 인해 app 객체 따로 선언 
server = Server()
app = server.app    
if __name__ == "__main__":
    app.run(debug=True)
    # server.app.run(debug=True)
    



